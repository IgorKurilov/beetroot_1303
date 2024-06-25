import asyncio
import uuid

# Словари для хранения информации о клиентах
clients = {}  # Сокеты клиентов
client_ids = {}  # Информация о клиентах

# функция для обработки каждого клиента
async def handle_client(reader, writer):
    # Генерация уникального ID для каждого клиента
    client_id = str(uuid.uuid4())
    addr = writer.get_extra_info('peername')
    clients[client_id] = writer
    client_ids[client_id] = {'name': str(addr)}
    print(f"[NEW CONNECTION] {client_id} connected from {addr}")

    try:
        while True:
            # Чтение данных от клиента
            data = await reader.read(100)
            message = data.decode().strip()

            if not message:
                break

            if message == "QUIT":
                # Обработка команды выхода из чата
                print(f"[DISCONNECT] {client_id} has disconnected by QUIT command")
                del clients[client_id]
                del client_ids[client_id]
                writer.close()
                await writer.wait_closed()
                await broadcast(f"{client_id} has left the chat.", client_id)
                break
            elif message == "ONLINE":
                # Обработка команды для получения списка клиентов
                online_clients = ', '.join([client_ids[client_id]['name'] for client_id in client_ids])
                writer.write(f"Online clients: {online_clients}\n".encode())
                await writer.drain()
            elif message.startswith("/name"):
                # Обработка команды для изменения имени пользователя
                new_name = message.split(" ", 1)[1]
                old_name = client_ids[client_id]['name']
                client_ids[client_id]['name'] = new_name
                await broadcast(f"{old_name} ({client_id}) has changed their name to {new_name}", client_id)
            elif message.startswith("/msg"):
                # Обработка команды отправки приватного сообщения
                parts = message.split(" ", 2)
                if len(parts) < 3:
                    writer.write("Usage: /msg <username> <message>\n".encode())
                    await writer.drain()
                else:
                    target_name, private_message = parts[1], parts[2]
                    await send_private_message(client_id, target_name, private_message)
            else:
                # Отправка обычного сообщения всем клиентам, кроме автора
                sender_name = client_ids[client_id]['name']
                await broadcast(f"{sender_name} ({client_id}): {message}", client_id)
    except Exception as e:
        print(f"Error: {e}")

    print(f"[DISCONNECT] {client_id} has disconnected")
    if client_id in clients:
        del clients[client_id]
    if client_id in client_ids:
        del client_ids[client_id]
    writer.close()
    await writer.wait_closed()

# функция для широковещательной рассылки сообщений
async def broadcast(message, sender_id=None):
    for client_id, writer in clients.items():
        if client_id != sender_id:  # Не отправлять сообщение его автору
            try:
                writer.write(message.encode())
                await writer.drain()
            except Exception as e:
                print(f"Error broadcasting message: {e}")

# функция для отправки приватного сообщения
async def send_private_message(sender_id, target_name, message):
    sender_name = client_ids[sender_id]['name']
    for client_id, info in client_ids.items():
        if info['name'] == target_name:
            writer = clients[client_id]
            try:
                writer.write(f"Private message from {sender_name} ({sender_id}): {message}\n".encode())
                await writer.drain()
            except Exception as e:
                print(f"Error sending private message: {e}")
            return
    sender_writer = clients[sender_id]
    sender_writer.write(f"User {target_name} not found.\n".encode())
    await sender_writer.drain()

# функция для запуска сервера
async def start_server():
    # Настройка и запуск сервера
    server = await asyncio.start_server(handle_client, '127.0.0.1', 5555)
    addr = server.sockets[0].getsockname()
    print(f"[STARTING] Server started on {addr}")

    # Ожидание и обработка подключений клиентов
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    try:
        # Запуск сервера
        asyncio.run(start_server())
    except KeyboardInterrupt:
        print("[SHUTDOWN] Server shutting down")

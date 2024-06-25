import asyncio

# функция для получения сообщений от сервера
async def receive_messages(reader):
    while True:
        # Чтение данных от сервера
        data = await reader.read(100)
        if not data:
            print("[DISCONNECTED] Server disconnected")
            break
        message = data.decode()
        print(message)

# функция для отправки сообщений на сервер
async def send_messages(writer):
    while True:
        # Чтение ввода пользователя и отправка сообщения на сервер
        message = input()
        writer.write(message.encode())
        await writer.drain()
        if message.strip() == "QUIT":
            print("[INFO] You have left the chat")
            writer.close()
            await writer.wait_closed()
            break

# функция для запуска клиента
async def start_client():
    # Подключение к серверу
    reader, writer = await asyncio.open_connection('127.0.0.1', 5555)

    # Создание асинхронных задач для получения и отправки сообщений
    receive_task = asyncio.create_task(receive_messages(reader))
    send_task = asyncio.create_task(send_messages(writer))

    # Ожидание завершения задач
    await asyncio.gather(receive_task, send_task)

if __name__ == "__main__":
    try:
        # Запуск клиента
        asyncio.run(start_client())
    except KeyboardInterrupt:
        print("[SHUTDOWN] Client shutting down")

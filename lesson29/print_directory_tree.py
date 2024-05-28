import os

def print_directory_tree(startpath, indent=''):
    """
    Рекурсивно друкує дерево директорій та файлів починаючи з вказаної директорії.
    
    Parameters:
    startpath (str): Початкова директорія, з якої починається побудова дерева.
    indent (str): Відступ для вкладених елементів. Використовується для візуалізації рівнів дерева.
    """
    # Проходимо по всіх елементах в поточній директорії
    for item in os.listdir(startpath):
        # Формуємо повний шлях до елемента
        path = os.path.join(startpath, item)
        # Якщо елемент є директорією, друкуємо його з іконкою 📁 та викликаємо функцію рекурсивно
        if os.path.isdir(path):
            # Якщо елемент є директорією (os.path.isdir(path)), друкуємо його з іконкою 📁.
            print(f"{indent}📁 {item}") 
            print_directory_tree(path, indent + '    ')
        # Якщо елемент є файлом, друкуємо його з іконкою 📄
        else:
            print(f"{indent}📄 {item}")

if __name__ == "__main__":
    # Друкуємо заголовок
    print("Структура поточної робочої папки:")
    # Отримуємо поточну робочу директорію
    current_working_directory = os.getcwd()
    # Викликаємо функцію для друку дерева директорій, починаючи з поточної робочої директорії
    print_directory_tree(current_working_directory)

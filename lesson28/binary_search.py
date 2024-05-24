# Реалізація бінарного пошуку за допомогою рекурсії
# Бінарний пошук працює на відсортованих масивах, розділяючи масив на половини та шукаючи елемент в одній з половин. 
# Рекурсивна реалізація бінарного пошуку виглядає наступним чином:
def binary_search(arr, target, low, high):
    if low > high:
        return -1  # Повертаємо -1, якщо елемент не знайдено

    mid = (low + high) // 2  # Знаходимо середній індекс

    if arr[mid] == target:
        return mid  # Якщо елемент знайдено, повертаємо його індекс
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)  # Шукаємо в лівій половині
    else:
        return binary_search(arr, target, mid + 1, high)  # Шукаємо в правій половині

# Приклад використання
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
result = binary_search(arr, target, 0, len(arr) - 1)
print("Element found at index:", result)

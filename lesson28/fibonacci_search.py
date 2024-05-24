# Fibonacci Search - це алгоритм пошуку, який використовує числа Фібоначчі для поділу масиву. 
# Цей алгоритм працює на відсортованих масивах і має складність O(log n), 
# подібно до бінарного пошуку, але використовує інший підхід до поділу масиву.
# Реалізація Fibonacci Search:
def fibonacci_search(arr, target):
    fib_m2 = 0  # (m-2)'e число Фібоначчі
    fib_m1 = 1  # (m-1)'e число Фібоначчі
    fib_m = fib_m2 + fib_m1  # m'е число Фібоначчі

    n = len(arr)

    while (fib_m < n):
        fib_m2 = fib_m1
        fib_m1 = fib_m
        fib_m = fib_m2 + fib_m1

    offset = -1

    while (fib_m > 1):
        i = min(offset + fib_m2, n - 1)

        if (arr[i] < target):
            fib_m = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m - fib_m1
            offset = i
        elif (arr[i] > target):
            fib_m = fib_m2
            fib_m1 = fib_m1 - fib_m2
            fib_m2 = fib_m - fib_m1
        else:
            return i

    if(fib_m1 and arr[offset + 1] == target):
        return offset + 1

    return -1

# Приклад використання
arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
target = 85
result = fibonacci_search(arr, target)
print("Element found at index:", result)

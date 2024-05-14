import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time of {func.__name__}: {execution_time:.6f} seconds")
        return result
    return wrapper

# Приклади реалізацій функцій для знаходження найбільшого спільного дільника

@measure_time
def gcd_subtraction(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

@measure_time
def gcd_modulus(a, b):
    while b != 0:
        a, b = b, a % b
    return a

@measure_time
def gcd_builtin(a, b):
    import math
    return math.gcd(a, b)

# Тестування різних реалізацій функцій з використанням декоратора для вимірювання часу

print("GCD using subtraction:")
print(gcd_subtraction(999999, 2))

print("GCD using modulus:")
print(gcd_modulus(999999, 2))

print("GCD using built-in function:")
print(gcd_builtin(999999, 2))

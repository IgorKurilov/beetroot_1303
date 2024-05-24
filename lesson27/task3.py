def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def quick_sort(arr, low, high, partition_limit):
    if low < high:
        if high - low <= partition_limit:
            insertion_sort(arr[low:high+1])
        else:
            pi = partition(arr, low, high)
            quick_sort(arr, low, pi - 1, partition_limit)
            quick_sort(arr, pi + 1, high, partition_limit)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
quick_sort(arr, 0, len(arr) - 1, partition_limit=5)
print("Sorted array:", arr)

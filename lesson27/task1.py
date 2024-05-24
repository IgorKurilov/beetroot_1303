def bidirectional_bubble_sort(arr):
    n = len(arr)
    swapped = True

    while swapped:
        swapped = False
        # Move "up" the list
        for i in range(0, n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        n -= 1
        # Move "down" the list
        for i in range(n - 1, 0, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True

    return arr

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bidirectional_bubble_sort(arr)
print("Sorted array:", sorted_arr)

def quick_sort(sequence):
    # Base case: if the sequence has 1 or fewer elements, it is already sorted
    if len(sequence) <= 1:
        return sequence

    # Choose the first element as the pivot
    pivot = sequence[0]
    # Partition the sequence into two sublists: elements smaller than pivot (left) and greater than or equal to pivot (right)
    left = [element for element in sequence[1:] if element < pivot]
    right = [element for element in sequence[1:] if element >= pivot]
    # Recursively sort the left and right sublists, and concatenate them with the pivot in between
    return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == "__main__":
    to_sort = [15, 9, 8, 1, 4, 11, 7, 12, 13, 6, 5, 3, 16, 2, 10, 14]
    print(quick_sort(to_sort))

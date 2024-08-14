def insert_sort(arr, n):
    """this function takes an array of size n and return 
    its sorted version
    Args:
        arr (array): array to be sorted
        n (int): size of the array

    Returns:
        array: sorted version of the initial input
    """
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key
    return arr

print(insert_sort([31, 41, 59, 26, 41, 58], 6))
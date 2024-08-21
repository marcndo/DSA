"""
SELECTION-SORT(A, n)
    for i = 0 to n
        min_index = i
        for j = i+1 to n
            A[j] < A[min_index]
            min_inded = j
        A[i], A[min_index] = A[min_index], A[i]
    return A
     
"""
def selection_sort(arr, n):
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(selection_sort([2, 5, 1, 9, 3], 5))


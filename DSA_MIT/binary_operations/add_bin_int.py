"""
ADD-BINARY-INTEGER(A,B, n)
    subtotal = []
    carry = 0
    for i = 0 to n
#access elements in A&B in reverse order.
       current_sum = A[i] + B[i] + carry
       sub_total.insert(0, current_sum%2)
       carry = current_sum//2
    if carry
        sub_total.insert(0, carry)
"""
def add_binary_integer(arr, arr1, n):
    sub_total = []
    carry = 0
    for i in range(n-1, -1, -1):
        current_sum = arr[i] + arr1[i] + carry
        sub_total.insert(0, current_sum%2)
        carry = current_sum//2
    if carry:
        sub_total.insert(0, carry)
    return sub_total


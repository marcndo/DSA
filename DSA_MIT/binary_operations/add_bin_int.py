"""
add binary integers Pseudo code
===============================
constraint: both arrays are of same length
ADD-BINARY-INTEGERS(l1, l2, n)
    sub_total = []
    add = 0
    l1 = l1[::-1]
    l2 = l2[::-1]
    for i in l1:
      for j in l2:
      if i == j
          add = l1[i] + l2[j]
          if add < 2
              sub_total.insert(add)
          else
              while i < n-1 and j < n-1
                  mod = (l1[i]+l[j]) % 2
                  quotient = (l1[i]+l[j])//2
                  sub_total.insert(mod)
                  add += quotient
              sub_total.insert(add%2)
              sub_total.insert(add//2)
    return sub_total    
"""
def add_binary_integer(arr1, arr2, n):
    sub_total = []
    add = 0
    arr1 = arr1[::-1]
    arr2 = arr2[::-1]
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if i == j:
                add = arr1[i] + arr2[j]
                if add < 2:
                    sub_total.insert(0, add)
                else:
                    while i < n-1:
                        mod = (arr1[i] + arr2[j])%2
                        quotient = (arr1[i] + arr2[j])//2
                        sub_total.insert(0, mod)
                        add +=quotient
                    sub_total.insert(0,add%2)
                    sub_total.insert(0,add//2)
    return sub_total

print(add_binary_integer([1, 0], [1, 1], 3))
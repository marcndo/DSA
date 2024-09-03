"""
CONTAIN-DUPLICATE(arr)
     hashset = set(arr)
     is_duplicated = false
     if len-arr > len-hashset
         is_duplicated = true
     return is_duplicated
"""


def contain_duplicate(items: list) -> bool:
    hashset = set(items)
    is_duplicated = False
    if len(items) > len(hashset):
        is_duplicated = True
    return is_duplicated







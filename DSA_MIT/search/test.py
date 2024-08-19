"""
pseudo code
============
LINEAR-SEARCH(arr, x)
    index = 0
    while index < len(arr) and arr[index] <= x
       if arr[index]== x
           return index
       else
           index +=1
"""
def linear_search(arr, x):
    """Return and index for a search item if foud in the list
    Args:
        arr (list): list of numbers
        x (int): searched item

    Returns:
        int: index of search item.
    """
    index = 0
    while index < len(arr) and arr[index] <= x:
        if arr[index] == x:
            return f"Search intem is in index {index}"
        else:
            index +=1
    return f'Item {x} not in the list'


"""
linear search algo
=====================
LINEAR-SEARCH(arr, search_item)
    index = 0
    if arr[index] == search_item
        return index
    else
        while index <=len(arr) and arr[index] < search_item
            index +=1
        return item not in list
"""

def linear_search(arr, search_item):
    search_index = 0
    print(search_index)
    if arr[search_index] == search_item:
        return search_index
    else:
        while search_index < len(arr) and arr[search_index] <= search_item:
            search_index +=1
    return 

print(linear_search([1, 3, 4, 5, 6, 7, 9], 9))
"""
Given a non-empty array of integers nums, every element
 appears twice except for one. Find that single one.
SINGLEONE(arr)
    hashset = set(arr)
    for i in hashset
        if count of i ==1
            return i
"""


def single_one(arr):
    hashset = set(arr)
    for i in hashset:
        if arr.count(i) == 1:
            return i


# Write a program to store the elements in 1-D array and provide an option to
# perform the operations like searching, sorting, merging, reversing the elements.

import numpy as np

arr = [15, 6, 17, 12, 9, 2]

def binary_search(arr, el, start, end):
    mid = (start + end) // 2
    if el == arr[mid]: 
        return mid
    if el < arr[mid]:
        return binary_search(arr, el, start, mid-1)
    else:
        return binary_search(arr, el, mid+1, end)

print(binary_search(arr, 12, 0, len(arr)))


def sorting(arr):
    arr.sort()
    return arr

print(sorting(arr))


def merge():
    a = [15, 6, 17, 12, 9, 2]
    b = [12, 33, 4]
    merged_list = np.concatenate((a,b))
    return merged_list
    
print(merge())


def rev():
    rev_list = np.flipud(arr)
    return rev_list
print(rev())





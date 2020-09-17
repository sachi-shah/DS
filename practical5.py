# Write a program to search an element from a list. Give user the option to perform
# Linear or Binary search


def linear_search(mylist, el):
    for i in mylist:
        if i == el:
            return mylist.index(i)
    return -1


def binary_search(mylist, el, start, end):
    mid = (start + end) // 2
    if el == mylist[mid]: 
        return mid
    if el < mylist[mid]:
        return binary_search(mylist, el, start, mid-1)
    else:
        return binary_search(mylist, el, mid+1, end)


mylist = [1, 2, 5, 7, 13, 15]
print(mylist)
n = input("searching for 5 \nEnter l for linear search and b for binary search: ")
el = 5
if n=='l':
    print(linear_search(mylist, el))
elif n=='b':
    print(binary_search(mylist, el, 0, len(mylist)))
else:
    print("invalid input")



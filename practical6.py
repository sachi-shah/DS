# WAP to sort a list of elements. Give user the option to perform sorting using Insertion
# sort, Bubble sort or Selection sort.


# Selection sort

def Selection_sort():
    mylist = [19, 27, 62, 24, 21, 2 ,51]

    print(mylist)
    for i in range(len(mylist)):
        min_val_index = i
        for j in range(i+1, len(mylist)):
            if mylist[min_val_index] > mylist[j]:
                min_val_index = j
        mylist[i], mylist[min_val_index] = mylist[min_val_index], mylist[i]
    return mylist


# Insertion sort

def Insertion_sort():
    mylist = [19, 27, 62, 24, 21, 2 ,51]
    
    print(mylist)
    for i in range(len(mylist)):
        val = mylist[i]
        j = i-1
        while j >= 0 and val < mylist[j]:
            mylist[j+1] = mylist[j]
            j -= 1
        mylist[j+1] = val
    return mylist
    

# Bubble sort

def Bubble_sort():
    mylist = [19, 27, 62, 24, 21, 2 ,51]
    
    print(mylist)
    for i in range(len(mylist)):
        for j in range(len(mylist) - 1):
            if mylist[j] > mylist[j+1]:
                mylist[j], mylist[j+1] = mylist[j+1], mylist[j]        
    return mylist


n = input("Enter s : selection sort , i : Insertion sort, b : bubble sort : ")
if n=='s':
    print("After selection sort: ", Selection_sort())
elif n=='i':
    print("After insertion sort: ", Insertion_sort())
elif n=='b':
    print("After bubble sort: ",Bubble_sort())
else:
    print("invalid input")





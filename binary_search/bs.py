def binarySearch(arr,target): #O(log2n)
    lindex=0
    rindex=len(arr)-1

    while lindex<=rindex:

        mid=(lindex+rindex)//2

        if (arr[mid]==target):
            return mid
        
        if arr[mid]<target:
            lindex=mid+1
        else:
            rindex=mid-1
            
    return -1

myArray = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
myTarget = 3

result = binarySearch(myArray, myTarget)

if result != -1:
    print("Value",myTarget,"found at index", result)
else:
    print("Target not found in array.")

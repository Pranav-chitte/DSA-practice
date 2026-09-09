def BinarySearch(arr,target):
    n= len(arr)
    l=0
    r=n-1
    while(l<=r):
        mid = (l+r)//2
        if(arr[mid]<target):
             l=mid+1
        elif(arr[mid]>target):
            r=mid-1
        else:
            return mid 
    return -1

arr=[2,4,6,8,7536,898989,909090909]

sorted_array= BinarySearch(arr,6)

print(sorted_array)
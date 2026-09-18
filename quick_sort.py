#quick_sort
def quick_sort(arr):
    if len (arr)<=1:
        return arr
    pivot = arr[-1]
    left = []
    right = []
    for element in arr [:-1]:
        if element <= pivot:
            left.append(element)
        else:
            right.append(element)
    return quick_sort(left) + [pivot] + quick_sort(right)
arr = [50,20,40,10,30]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr) s
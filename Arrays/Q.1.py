#  Find the Largest Element in an Array

def find_largest_element(arr):
    if not arr:
        return None
    
    return max(arr)


arr = [34,454,34,54,34]
print(find_largest_element(arr))


# or

def find_min_max(arr):
    max = arr[0]
    min = arr[0]

    for i in range(len(arr)):
        if arr[i] > max:
            max +=arr[i]
        elif arr[i] < min:
            min+=arr[i]

    print("Max element :", max)
    print("Min element :" ,min)

arr = [56,98,23,100 ,45,677]
find_min_max(arr)



    
    
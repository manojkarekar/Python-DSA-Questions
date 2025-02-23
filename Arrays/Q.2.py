
# array rotation to the right side.

def array_rotation(arr,k):
    k%=len(arr)
    return arr[-k:] + arr[:-k]                                                                                                                                                                                                                                                                                                                                                                                               

arr = [1,2,3,4,5]
k = 2 
x  = array_rotation(arr,k)
print(x)

 

# array rotation to the left side 

def array_rotation_left_side(arr,k):
    k%=len(arr)

    return arr[k:] + arr[:k]

arr2 = [1,2,3,4,5]
p = array_rotation_left_side(arr2,2)
print(p)



def rotate_array(arr, k):
    print("original array",arr)
    # k%=len(arr)
    # reversed(arr[])  

    arr[:] = list(reversed(arr))
    print("After reversed arrry",arr)
    arr[:k] = list(reversed(arr[:k]))
    
    arr[k:] = list(reversed(arr[k:]))

    return arr

arr = [1, 2, 3, 4, 5, 6, 7]
k = 6

x = rotate_array(arr,k)
print(x)


# without using revrsed method  
# 
# def rotate_array_right(arr,k):
    # k%=len(arr)
# 
    # for i in range(0,k):
        # arr[i] = arr[]
        # print(i)
    # print(arr)
# 
# rotate_array_right([1,2,3,4,5],2)







def reverse_array(arr,start,end):
    while start<end:
        
        arr[start] , arr[end] = arr[end] , arr[start]
        start+=1 
        end-=1 
    return arr
    

def Right_array_rotation(arr,k):
    start = 0
    end = len(arr) - 1  
    k%=len(arr)

    print("Original Array : ",arr)

    reverse_array(arr,start,end)
    
    reverse_array(arr,start,k-1)

    reverse_array(arr,k,end)

    return arr
    

arr = [1,2,3,4,5]
k =  3

result = Right_array_rotation(arr,k)
print("Right array rotation : ",result)


def Left_array_rotation(arr,k):
    start = 0
    left = len(arr)-1
    k%=len(arr)

    print("Original array : ",arr)

    pass


arr = [7,6,8,2,9,1,4]
k = 2

result = Left_array_rotation(arr,k)

print("Left Array rotation : ",result)  
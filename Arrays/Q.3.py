# Reverse the elements of the array in place.

arr = [1,2,3,4,5,6,7]

reversed_arr = []
for i in range(len(arr)-1,-1,-1):
    reversed_arr.append(arr[i])


print("Original Array:",arr)
print("Reversed Array:",reversed_arr)

# ------------------------------------------------------
# reverse array with swaping number 
def reverse_array(arr):
    start = 0 
    end = len(arr2)-1
    while start < end:
        arr[start] , arr[end] = arr[end] , arr[start]

        start+=1
        end-=1

    return arr

arr2 = [89,45,23,76,45,45,64]
ans  = reverse_array(arr2)
print(ans)

# ------------------------------------------------------
# reverse array with for loop 

def reversed_array(arr,start,end):
    print(len(arr) //2)
    for i in range(len(arr)//2):
        arr[start] , arr[end] = arr[end] , arr[start]
        start +=1
        end-=1

    return arr



arr = [54,89,23,65,90,78]
start = 0 
end = len(arr)-1

x  = reversed_array(arr,start,end)
print(x)
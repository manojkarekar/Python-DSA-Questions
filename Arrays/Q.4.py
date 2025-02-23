# 3. Find the Sum of All Elements in an Array

def sum_of_array(arr):
    sum = 0 
    for i in arr:
        sum += i
    
    return sum

arr = [24,34,34,5,4,34]

x = sum_of_array(arr)
print(x)
        
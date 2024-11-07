#Problem: Print All Sub-arrays of an Array

#Declaring the Function
def print_all_subarrays(arr):
    n = len(arr)
    for start in range(n):
        for end in range(start, n):
            print(arr[start:end+1])


#Implementation
array = [1, 2, 3, 4]
print_all_subarrays(array)

def max_subarray_sum(array):
    max_sum = float("-inf")  #represents negative infinity
    current_sum = 0
    length = len(array)
    for i in range(length):
        current_sum += array[i]
        max_sum = max(max_sum, current_sum)
        if current_sum < 0:
            current_sum = 0
    return max_sum

#Implementation
#Declaring the Array
array = [3, -4, 5, 4, -1, 7, -8]
result = max_subarray_sum(array) #Calling the Function
print("Maximum Subarray Sum:", result) #Output Maximum Subarray Sum



# 2nd Version: Maximum Subarray Sum using Kadane's Algorithm
# def max_subarray_sum_kadane(arr):
#     max_so_far = arr[0]  # Initialize with the first element
#     current_max = arr[0]
    
#     for i in range(1, len(arr)):
#         current_max = max(arr[i], current_max + arr[i])
#         max_so_far = max(max_so_far, current_max)
    
#     return max_so_far

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
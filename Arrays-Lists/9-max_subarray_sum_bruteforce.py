#Declaring the Function for Maxium Subarray Sum
def max_subarray_sum(arr):
    max_sum = float('-inf')   #represents negative infinity
    length = len(arr)   #Finding the length of the array

    for start in range(length):    #Iterating through the array
        current_sum = 0  #Initializing the current sum
        for j in range(start, length):  #Iterating through the array
            current_sum += arr[j]   #Adding the elements of the array
            max_sum = max(max_sum, current_sum)    #Finding the maximum sum
    return max_sum

#Implementation
#Declaring the Array
array = [3, -4, 5, 4, -1, 7, -8]
result = max_subarray_sum(array) #Calling the Function
print("Maximum Subarray Sum:", result) #Output Maximum Subarray Sum


def majority_element(arr):
    #Sort the array
    arr.sort()
    
    #Initialize counting variables
    current_element = arr[0]
    current_count = 1
    length = len(arr)
    
    #Loop through the sorted array to count occurrences
    for i in range(length):
        if arr[i] == current_element:
            current_count += 1
        else:
            # Reset count for a new element
            current_element = arr[i]
            current_count = 1
        
        #Check if current element's count exceeds n / 2
        if current_count > length // 2:
            return current_element
    
    # The function should return before this point as the majority element is guaranteed to exist
    return None




#Implementation
arr = [3, 2, 4, 4, 4, 4, 3]
length = len(arr)
print(f"Array: {arr},\nArray Length: {length}")
result = majority_element(arr)
print("Majority Element in an Array is =", result)  # Print the array
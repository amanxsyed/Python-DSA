def find_max_and_min(arr):
    # Step 1: Check if the array is empty
    if len(arr) == 0:  # Instead of if not arr, we check the length
        return None, None  # Return None for both max and min if the array is empty

    # Step 2: Assume the first element is both max and min
    max_number = arr[0]
    min_number = arr[0]

    # Step 3: Go through each number in the array
    for number in arr:
        # Step 4: Check if the current number is greater than max_value
        if number > max_number:
            max_number = number  # Update max_value if found a new maximum
        
        # Step 5: Check if the current number is less than min_value
        if number < min_number:
            min_number = number  # Update min_value if found a new minimum

    # Step 6: Return the maximum and minimum values found
    return max_number, min_number

#Main Implementation
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
max_result, min_result = find_max_and_min(numbers)
print("Maximum Number:", max_result)
print("Minimum Number:", min_result)

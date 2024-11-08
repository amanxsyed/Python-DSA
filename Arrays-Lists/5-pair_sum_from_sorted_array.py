def find_pair_with_sum(arr, target):
    # Step 1: Sort the array
    arr.sort()
    
    # Step 2: Initialize pointers
    left = 0
    right = len(arr) - 1

    # Step 3: Traverse the array with two pointers
    while left < right:
        # Step 4: Calculate the current sum of elements at pointers
        current_sum = arr[left] + arr[right]

        # Step 5: Check if current sum is equal to the target
        if current_sum == target:
            return (arr[left], arr[right])  # Return the pair if the target sum is found

        # Step 6: Move pointers based on the current sum
        elif current_sum < target:
            left += 1  # Move left pointer to the right to increase the sum
        else:
            right -= 1 # Move right pointer to the left to decrease the sum

    # Step 7: Return None if no pair is found
    return None

#Implementation
arr = [1, 2, 3, 4, 8, 10, 6]
length = len(arr)
target = 6
print(f"Array: {arr},\nArray Length: {length},\nTarget: {target}")
result = find_pair_with_sum(arr, target)
print(result)  # Print the array

def binary_search(arr, target):
    # Step 1: Initialize the search range
    start = 0
    end = len(arr) - 1
    
    # Step 2: Loop continues until start > end
    while start <= end:
        # Step 3: Find the middle index of Array
        mid = start + (end - start) // 2   # This ensures no overflow when working with large numbers.

        # Step 4: If the target is larger, search in the right half
        if arr[mid] < target:
            start = mid + 1  
        
        # Step 5: If the target is smaller, search in the left half
        elif arr[mid] > target:
            end = mid - 1
        
        # Step 6: Check if the middle element is the target value which we are finding
        else:
            return mid, arr[mid] # Return index and value if found
    
    # Step 7: If not found, return -1 or Element not Found
    return -1, "Element not Found in an Array"

# Test the function
arr = [2, 4, 6, 8, 10, 12, 14]
target = 7

# Searching for the target
index, value = binary_search(arr, target)
print(f"Index: {index}, Value: {value}")  

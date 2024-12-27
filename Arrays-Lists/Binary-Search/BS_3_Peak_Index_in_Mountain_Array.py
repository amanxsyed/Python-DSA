def peak_index_in_mountain_array(arr):
    # Start searching from index 1 to len(arr) - 2, because the peak cannot be at the boundaries
    start, end = 1, len(arr) - 2  
    
    while start < end:
        # Find the middle index
        mid = start + (end - start) // 2
        
        # Compare the middle element with the next element
        if arr[mid] < arr[mid + 1]:
                # If the middle element is less than the next one,
                # the peak must be in the right half
            start = mid + 1
        else:
            # If the middle element is greater than or equal to the next one,
            # the peak must be in the left half or at the middle
            end = mid - 1
    
    # After the loop, start == end, which is the peak index
    # Return the index and the corresponding element
    return start, arr[start]

# Implementation:
arr = [0, 3, 8, 9, 4, 2]
index, peak = peak_index_in_mountain_array(arr) 

print(f"Peak Element {peak} found at index {index}.") 

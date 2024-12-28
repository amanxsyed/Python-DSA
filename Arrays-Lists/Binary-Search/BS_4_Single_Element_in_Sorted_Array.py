def singleNonDuplicate(nums):
    n = len(nums)
    start = 0 
    end = len(nums) - 1
    
    if n == 1:
        return nums[0]

    # Perform binary search
    while start < end:
        # Find the mid element (avoiding overflow)
        mid = start + (end - start) // 2
        
        # Special case: if mid is the first element and not equal to the second element
        if mid == 0 and nums[0] != nums[1]:
            return nums[mid]
        
        # Special case: if mid is the last element and not equal to the second last element
        if mid == n - 1 and nums[n-1] != nums[n-2]:
            return nums[mid]
        
        # Check if the mid element is the single element
        if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
            return nums[mid]
        
        # Determine which half to search next
        # Case: mid is even
        if mid % 2 == 0:
            # If mid matches its previous element, the single element is in the left half
            if nums[mid-1] == nums[mid]:
                end = mid - 1
            # Otherwise, it's in the right half
            else:
                start = mid + 1
        # Case: mid is odd
        else:
            # If mid matches its previous element, the single element is in the right half
            if nums[mid-1] == nums[mid]:
                start = mid + 1
            # Otherwise, it's in the left half
            else:
                end = mid - 1

    # If no single element is found, return -1
    return -1

# Implementation
nums = [1, 1, 3, 3, 4, 4, 5, 8, 8]
print("Single element:", singleNonDuplicate(nums))

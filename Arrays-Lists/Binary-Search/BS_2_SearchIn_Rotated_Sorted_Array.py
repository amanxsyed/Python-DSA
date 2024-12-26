def search_rotated_array(arr, target):
    # Declare the start and end indices 
    st = 0
    end = len(arr) - 1

    while st <= end:
        # Find the middle index
        mid = st + (end - st) // 2    # Using (end - st) prevents integer overflow

        # Check if the middle element is the target
        if arr[mid] == target:
            return mid

        # Determine which half is sorted
        if arr[st] <= arr[mid]:  # Left half is sorted
            if arr[st] <= target < arr[mid]:  # Target lies in the left half
                end = mid - 1
            else:  # Target lies in the right half
                st = mid + 1
        else:  # Right half is sorted
            if arr[mid] < target <= arr[end]:  # Target lies in the right half
                st = mid + 1
            else:  # Target lies in the left half
                end = mid - 1

    return -1  # Target not found

#Implementation:

    # Rotated sorted array
arr = [3, 4, 5, 6, 7, 0, 1, 2]
target = 0

    # Search for the target
result = search_rotated_array(arr, target)

if result != -1:
    print(f"Target {target} found at index {result}.")
else:
    print(f"Target {target} not found in the array.")

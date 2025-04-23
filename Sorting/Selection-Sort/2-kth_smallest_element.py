def kth_smallest(arr, k): 
    # Function to find the kth smallest element in an array using Selection Sort
    # This function modifies the original array to sort it and then returns the kth smallest element.
    # It uses the Selection Sort algorithm to sort the array in ascending order.
    # The kth smallest element is then simply the element at index k-1 in the sorted array.

    n = len(arr) # Get the length of the list
    # Check if k is within the bounds of the array
    if k <= 0 or k > n:
        return None  # Return None if k is out of bounds
    # The outer loop iterates through the first k elements of the array
    for i in range(k):
        min_index = i # Assume the first element of the unsorted part is the minimum
        # The inner loop finds the minimum element in the unsorted part of the array
        for j in range(i + 1, n):
            # Compare to find the minimum element
            if arr[j] < arr[min_index]:     # change sign to > for descending order
                min_index = j    # Update min_index if a smaller element is found
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr[k - 1]  # Return the kth smallest element (k-1 index in 0-based indexing)


if __name__ == "__main__":
    # Example usage
    arr = [7, 10, 4, 3, 20, 15]
    k = 2  # Find the 2nd smallest element
    print("Original array:", arr)
    print("2nd smallest element is:", kth_smallest(arr, k))
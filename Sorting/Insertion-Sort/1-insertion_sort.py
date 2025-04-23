def insertion_sort(arr):
    # Traverse through all array elements starting from the second element
    for i in range(1, len(arr)):
        key = arr[i]  # The current element to be inserted into the sorted portion
        j = i - 1  # The last index of the sorted portion
        
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift element to the right
            j -= 1
        
        # Insert the key at the correct position
        arr[j + 1] = key

if __name__ == "__main__":
    # Example usage:
    arr = [12, 11, 13, 5, 6]
    insertion_sort(arr)
    print("Sorted array is:", arr)

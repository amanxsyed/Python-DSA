def bubble_sort_desc(arr):
    # Bubble Sort algorithm to sort an array in descending order
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        swapped = False
        # Last i elements are already sorted, no need to check them
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                # Swap if the element found is less than the next element
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no two elements were swapped in the inner loop, then break
        if not swapped:
            break
    return arr

# This is a simple test case to demonstrate the bubble sort function
# The function can be called with an array of integers to sort them in ascending order.

if __name__ == "__main__":
    # Example usage
    arr = [56, 89, 49, 435, 62, 51, 88]
    print("Original array:", arr)
    desc_arr = bubble_sort_desc(arr)
    print("Sorted array is:", desc_arr)

# The time complexity of Bubble Sort is O(n^2) in the worst and average case, and O(n) in the best case (when the array is already sorted).

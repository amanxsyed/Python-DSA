def is_sorted(arr):
    # Check if the array is already sorted in ascending order
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True



def bubble_sort(arr):
    # Bubble Sort algorithm to sort an array in ascending order
    n = len(arr)
    swap_count = 0  # Initialize swap counter
    
    if is_sorted(arr):
        print("Array is already sorted.")
        return arr

    # Traverse through all array elements
    for i in range(n):
        swapped = False
        # Last i elements are already sorted, no need to check them
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                swap_count += 1  # Increment the swap counter whenever a swap is done
        # If no two elements were swapped in the inner loop, then break
        if not swapped:
            break
    print("Number of swaps:", swap_count)  
    return arr

# This is a simple test case to demonstrate the bubble sort function
# The function can be called with an array of integers to sort them in ascending order.

if __name__ == "__main__":
    # Example usage
    arr = [56, 89, 49, 435, 62, 51, 88]
    print("Original array:", arr)
    sorted_arr = bubble_sort(arr)
    print("Sorted array is:", sorted_arr)

# The time complexity of Bubble Sort is O(n^2) in the worst and average case, and O(n) in the best case (when the array is already sorted).

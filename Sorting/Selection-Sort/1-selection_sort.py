def selection_sort(arr):
    # Selection Sort algorithm to sort an array in ascending order
    # This algorithm divides the input list into two parts: a sorted part and an unsorted part.
    # It repeatedly selects the smallest (or largest, depending on the order) element from the unsorted part and moves it to the sorted part.
   
   
    n = len(arr)          # Get the length of the list
    # The outer loop iterates through the entire array
    for i in range(n): 
        min_index = i     # unsorted part starting
        # The inner loop finds the minimum element in the unsorted part of the array
        # It starts from the next element after i and goes to the end of the array
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:  # Compare to find the minimum element 
                #same as arr[j] > arr[min_index] for descending order
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap with the minimum element found
    # After the inner loop, the smallest element is placed at the beginning of the unsorted part
    return arr


if __name__ == "__main__":
    # Example usage
    arr = [56, 89, 49, 435, 62, 51, 88]
    print("Original array:", arr)
    sorted_arr = selection_sort(arr)
    print("Sorted array is:", sorted_arr)

# The time complexity of Selection Sort is O(n^2) in all cases (worst, average, and best).
# The space complexity is O(1) as it sorts the array in place.

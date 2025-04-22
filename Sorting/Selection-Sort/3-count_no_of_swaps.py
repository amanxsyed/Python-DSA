def selection_sort(arr):
    # Selection Sort algorithm to sort an array in ascending order
    n = len(arr)
    swap_count = 0  # Initialize swap counter

    for i in range(n): 
        min_index = i  # Assume current i is the minimum
        
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Only swap if a new min_index was found
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swap_count += 1  # Increment swap counter

        print(f"Pass {i + 1}: {arr} | Swaps so far: {swap_count}")

    print("Total swaps performed:", swap_count)
    return arr


if __name__ == "__main__":
    arr = [1,2,2,3,4]
    print("Original array:", arr)
    sorted_arr = selection_sort(arr)
    print("Sorted array is:", sorted_arr)
    
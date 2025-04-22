def bubble_sort_strings(arr):
    # Get the length of the list
    n = len(arr)
    
    # Outer loop for all elements in the list
    for i in range(n):
        # Inner loop to compare adjacent elements
        for j in range(0, n - i - 1):
            # Compare lowercase versions to make sorting case-insensitive
            if arr[j].lower() > arr[j + 1].lower():
                # Swap if the current word comes after the next one alphabetically
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    # Return the sorted list
    return arr


# Only runs when this file is executed directly (not when imported)
# This is a simple test case to demonstrate the bubble sort function
if __name__ == "__main__":
    # Take input from the user as a single string
    user_input = input("Enter words separated by spaces: ")
    
    # Split the input string into a list of words
    words = user_input.split()

    # Show the original list
    print("Original:", words)
    
    # Call the sorting function and store the result
    sorted_words = bubble_sort_strings(words)

    # Print the sorted list
    print("Alphabetically sorted:", sorted_words)

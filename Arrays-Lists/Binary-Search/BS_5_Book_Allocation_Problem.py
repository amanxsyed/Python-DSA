# Function to check if it is possible to allocate books such that no student reads more than max_allowed_pages
def is_valid(arr, n, students, max_allowed_pages):
    student_count = 1  # Start with the first student
    pages = 0  # Current sum of pages for the student

    for i in range(n):
        # If a single book has more pages than max_allowed_pages, allocation is not possible
        if arr[i] > max_allowed_pages:
            return False
        
        # If adding the current book's pages does not exceed max_allowed_pages, assign to current student
        if pages + arr[i] <= max_allowed_pages:
            pages += arr[i]
        else:
            # Assign books to the next student
            student_count += 1
            pages = arr[i]
            
            # If the number of students exceeds the limit, allocation is not possible
            if student_count > students:
                return False

    return True  # Allocation is possible with the given max_allowed_pages


# Main function to allocate books to students
def allocate_books(arr, n, students):
    # If the number of students is greater than the number of books, allocation is not possible
    if students > n:
        return -1

    # Calculate the sum of all pages (end of search space) and maximum single book pages (start of search space)
    total_pages = sum(arr)
    max_pages = max(arr)

    # Initialize the binary search range
    st = max_pages  # Minimum possible value for max_allowed_pages
    end = total_pages  # Maximum possible value for max_allowed_pages
    ans = -1  # Variable to store the final result

    # Binary search for the minimum maximum pages
    while st <= end:
        mid = st + (end - st) // 2  # Midpoint of the current range

        # Check if it is possible to allocate books with mid as the maximum allowed pages
        if is_valid(arr, n, students, mid):
            ans = mid  # Update the answer
            end = mid - 1  # Try for a smaller maximum value
        else:
            st = mid + 1  # Increase the maximum allowed pages

    return ans  # Return the minimized maximum pages


#Implementation
books = [10, 20, 30, 40]  # Array of pages in books
n = len(books)  # Number of books
students = 2  # Number of students

result = allocate_books(books, n, students)
print("Minimum maximum pages a student reads:", result)

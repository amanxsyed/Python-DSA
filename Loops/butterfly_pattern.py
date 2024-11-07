
#Declaring the Function to print butterfly of asterisk *
def print_butterfly_pattern(rows):
    #Upper Half Loop
    for i in range(1, rows + 1):
        for j in range(1, 2* rows):  # Inner loop for columns, spanning twice the number of rows
            if j<=i or j>=2* rows- i:  # Condition to print '*' on both left and right sides
                print('*', end=' ')  # Print star with space, keeping cursor on the same line
            else:
                print(' ', end=' ')   # Print space between the stars
        print() # Move to the next line after each row
    
    #Lower Half Loop
    for i in range(rows - 1, 0, -1):
        for j in range(1, 2* rows):   # Inner loop for columns, spanning twice the number of rows
            if j<=i or j>=2* rows- i:  # Condition to print '*' on both left and right sides
                print('*', end=' ')   # Print star with space, keeping cursor on the same line
            else:
                print(' ', end=' ')   # Print space between the stars
        print() # Move to the next line after each row

#Taking input from user
rows = int(input("Enter the number of rows: "))

#Calling the function
print_butterfly_pattern(rows)










#another approach of declaring function is given below
# Function to print the butterfly pattern

# def print_butterfly_pattern(n):
#     # Upper half of the butterfly
#     for i in range(1, n + 1):
#         # Print left side stars
#         for j in range(1, i + 1):
#             print("*", end="")
#         # Print spaces in the middle
#         for j in range(1, (2 * n) - (2 * i) + 1):
#             print(" ", end="")
#         # Print right side stars
#         for j in range(1, i + 1):
#             print("*", end="")
#         print()  # Move to the next line after each row

#     # Lower half of the butterfly
#     for i in range(n, 0, -1):
#         # Print left side stars
#         for j in range(1, i + 1):
#             print("*", end="")
#         # Print spaces in the middle
#         for j in range(1, (2 * n) - (2 * i) + 1):
#             print(" ", end="")
#         # Print right side stars
#         for j in range(1, i + 1):
#             print("*", end="")
#         print()  # Move to the next line after each row





# for i in range(5):
#     for j in range(6):
#         print("*", end=" ")
#     print()


# Function to print a solid rectangle
def print_rectangle(rows, columns):
    for i in range(rows):
        for j in range(columns):
            print("*", end=" ")  # Print star and stay on the same line
        print()  # Move to the next line after printing each row

# Example usage
rows = 5
columns = 10
print_rectangle(rows, columns)


#declare function
def print_half_pyramid_triangle(rows):
    for i in range(1, rows + 1):        #outer loop for rows
        for j in range(1, i + 1):       #inner loop for printing stars in each row
            print("*", end=" ")         # print stars without new-line
        print()                         # move to next line after print stars in each row

# Example usage
rows = 5
#calling the function
print_half_pyramid_triangle(rows)

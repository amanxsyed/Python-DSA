#Declaring the Function to print 0 1 Triangle
def print_zero_one_triangle(rows):
    for i in range(1, rows + 1): #outer loop for rows of patterns
        for j in range(1, i + 1): # inner loop to print numbers as per the row number
            print(j % 2, end=" ")
        print()  #prints next line

#Declaring the variable
rows = 5
#Calling the Function
print_zero_one_triangle(rows)
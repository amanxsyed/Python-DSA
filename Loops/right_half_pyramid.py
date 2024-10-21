#Declaring the Function to print Right Half Pyramid
def print_right_half_pyramid(n):
    for row in range(1, n+1):
        for spaces in range(n-row):
            print(' ', end=' ')
        for stars in range(row):
            print('*', end=' ')
        print()

#Declaring the variable n for number of rows
n = 5
#Calling the function
print_right_half_pyramid(n)
# Declaring the Function to print pyramid of numbers
def print_num_pyramid(num):
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
#Declaring the variable
num = 5
#Calling the function to print pyramid of numbers
print_num_pyramid(num)
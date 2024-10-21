#Declaring the function to print num pyramid
#approach of this function is different than inverted half pyramid asterisk(*) program
def print_inverted_num_pyramid(num):
    for i in range(num):
        for j in range(1, num - i + 1):
            print(j, end=" ")
        print()
#Declaring the variable
num = 5
#Calling the function to print num pyramid
print_inverted_num_pyramid(num)
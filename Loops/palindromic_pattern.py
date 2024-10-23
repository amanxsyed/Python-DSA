def print_num_pyramid(num):
    for i in range(1, num + 1):
        for j in range(1, num - i + 1):
            print(" ", end="")
        for j in range(i,0,-1):
            print(j, end="") 
        for j  in range(2, i + 1):
            print(j, end="")


        # Move to the next line after each row is printed
        print()

num = int(input("Enter the number to make a Palindromic Pyramid: "));


print_num_pyramid(num)
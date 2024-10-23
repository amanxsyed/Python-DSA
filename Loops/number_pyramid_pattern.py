def print_num_pyramid(num):
    for i in range(1, num + 1):
        for j in range(1, num - i + 1):
            print(" ", end="")
        for j in range(1, i + 1):
            print(i, end="")  # Print the row number 'i'

            if j < i:  # Add a space between the numbers, but not after the last one
                print(" ", end="")

        # Move to the next line after each row is printed
        print()

num = int(input("Enter the number to make a pyramid: "));


print_num_pyramid(num)
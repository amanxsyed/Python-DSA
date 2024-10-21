def print_inverted_half_pyramid(rows):
    for i in range(rows, 0 , -1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()

rows = 5
print_inverted_half_pyramid(rows)
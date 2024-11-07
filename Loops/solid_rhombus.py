def print_solid_rhombus(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1  - i):
            print(" " , end = " ")
        for j in range(1, n + 1):
            print("*", end = " ")
        print()

n = 5;

print_solid_rhombus(5)
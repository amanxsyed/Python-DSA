# Write a program to print the Floyd's Triangle.

#Declaring Function for Floyd Triangle

def floyd_triangle(rows):
    number = 1
    for i in range(1, rows + 1): #outer loop for rows of patterns
        for j in range(1, i + 1): # inner loop to print numbers as per the row number
            print(number, end=" ")
            number += 1 #number = number + 1
        print()  #prints next line

#Declaring the variable
rows = 5



#Calling the function to print Floyd Triangle
floyd_triangle(rows)

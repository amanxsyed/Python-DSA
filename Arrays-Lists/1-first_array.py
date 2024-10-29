#Write a Python program to create an array of 5 integers and display the array items.
# Create an array of 5 integers
arr = [10, 20, 30, 40, 50]

new_item = 60
arr.append(new_item)

# Display only the first 3 items using a loop
for i in range(6):
    print(arr[i])

def majority_element(arr):
    length = len(arr)
    #loop through each element in the array
    for i in range(length):
        count = 0 
        for j in range(length):

            #check if the element at index i is equal to the element at index j
            if arr[i] == arr[j]:
                count += 1

        #check if the count is greater than half the length of the array
        if count > length/2:
            return arr[i]  # Return the majority element if found
    return "No majority element found"





#Implementation
arr = [3, 2, 4, 4, 4, 4, 3]
length = len(arr)
print(f"Array: {arr},\nArray Length: {length}")
result = majority_element(arr)
print("Majority Element in an Array is =",result)  # Print the array
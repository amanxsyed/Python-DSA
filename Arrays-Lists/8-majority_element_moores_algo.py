def majority_element_moores_voting(arr):
    candidate = None
    count = 0
    
    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    
    for num in arr:
        if num == candidate:
            count += 1
    
    if count > len(arr) // 2:
        return candidate

    return None



#Implementation
arr = [3, 2, 4, 4, 4, 4, 3]
length = len(arr)
print(f"Array: {arr},\nArray Length: {length}")
result = majority_element_moores_voting(arr)
print("Majority Element in an Array is =", result)  # Print the array
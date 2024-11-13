def binarySearch(list1, start_index, end_index, target):
    # Base case: If the start index exceeds the end index, target is not found
    if start_index > end_index:
        return -1
    
    # Calculate the midpoint correctly
    mid = (start_index + end_index) // 2

    # Check if the target is found at the midpoint
    if list1[mid] == target:
        return mid
    # If target is less than the midpoint value, search in the left half
    elif target < list1[mid]:
        return binarySearch(list1, start_index, mid - 1, target)
    # If target is greater than the midpoint value, search in the right half
    else:
        return binarySearch(list1, mid + 1, end_index, target)
list1 =  [5,7,7,8,8,10]
target = 8
result = binarySearch(list1, 0, len(list1) - 1, target)
print("Target found at index:", result)  # Should print: Target found at index: 2

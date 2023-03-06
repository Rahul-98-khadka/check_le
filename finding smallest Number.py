def find_smallest(lst):
    # Initialize the smallest number to the first element of the list
    smallest = lst[0]
    
    # Iterate over the list and compare each element with the smallest number
    for num in lst:
        if num < smallest:
            smallest = num
    
    return smallest

list1 = [5, 7, 9, 14, 10, 20, 4]
print("The smallest number in the list is:", find_smallest(list1))

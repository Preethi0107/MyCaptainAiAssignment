def positive_numbers(list1):
    return [i for i in list1 if i > 0]

list1 = [12, -7, 5, 64, -14]
print("Input: ", list1)
print("Output: ", positive_numbers(list1))

list2 = [12, 14, -95, 3]
print("Input: ", list2)
print("Output: ", positive_numbers(list2))

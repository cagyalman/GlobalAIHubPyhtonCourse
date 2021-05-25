"""
AI720 - Ödev 1
Çağdaş Yalman

"""

""" 1 - Create two lists. The first list should consist of odd numbers.
The second list is should consist of even numbers. """

first_list = [1, 3, 5, 7, 9]
second_list = [2, 4, 6, 8]

""" 2 - Merge these two lists. Multiply all values in the new list by 2. """

first_list.extend(second_list)
first_list.sort()
print(first_list)

first_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = []

for i in first_list:
    new_list.append(i*2)
print(new_list)

""" 3 -  Use a loop to print the data type of the all values in the new list. """

print(len(new_list))

for i in new_list:
    if i == 9:
        break
    print(type(i))


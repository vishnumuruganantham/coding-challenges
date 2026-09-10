"""Sort a list
Input: [5,3,8,1,9]
Output: [1,3,5,8,1,9]
"""

list_input = [5, 3, 8, 1, 9]


def sort(list_input):
    list_input.sort()  # list.sort(), sorts in place
    return list_input


def sort_1(list_input):
    output = sorted(list_input)  # sorted(list) returns a new sorted array
    return output


def bubble_sort(list_input):
    n = len(list_input)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if list_input[j] > list_input[j + 1]:
                list_input[j], list_input[j + 1] = list_input[j + 1], list_input[j]
    return list_input


print(list_input)
print(sort(list_input))
print(sort_1(list_input))
print(bubble_sort(list_input))

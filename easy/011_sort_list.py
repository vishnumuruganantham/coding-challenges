"""Sort a list
Input: [5,3,8,1,9]
Output: [1,3,5,8,1,9]
"""

input = [5, 3, 8, 1, 9]


def sort(input):
    input.sort()  # list.sort(), sorts in place
    return input


def sort_1(input):
    output = sorted(input)  # sorted(list) returns a new sorted array
    return output


def bubble_sort(input):
    n = len(input)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if input[j] > input[j + 1]:
                input[j], input[j + 1] = input[j + 1], input[j]
    return input


print(input)
print(sort(input))
print(sort_1(input))
print(bubble_sort(input))

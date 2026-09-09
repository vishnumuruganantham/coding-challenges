"""
Input: "the sky is blue"
Output: "blue is sky the"

"""


def reverse_words(s):

    if not s:
        return None

    lst = s.split(" ")
    result = []

    for i in range(len(lst) - 1, -1, -1):
        result.append(lst[i])

    return " ".join(result)


print(reverse_words("the sky is blue"))

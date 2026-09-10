"""
Input:  'the sky is blue'
Output: 'eul bsi yk seht'
"""

# Reverse the string keeping the spaces


def reverse_string_keep_spaces(s):
    # Convert string to a list since strings are immutable in Python
    chars = list(s)

    left = 0
    right = len(chars) - 1

    while left < right:
        # Move the left pointer if it points to a space
        if chars[left] == " ":
            left += 1
        # Move the right pointer if it points to a space
        elif chars[right] == " ":
            right -= 1
        # Swap characters when both pointers point to non-space characters
        else:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

    return "".join(chars)


# Example usage
input_str = "the sky is blue"
output_str = reverse_string_keep_spaces(input_str)

print(f"Input:  '{input_str}'")
print(f"Output: '{output_str}'")

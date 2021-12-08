def reverse_str_recursive(input_str):
    if input_str=="": ##base case to end recursion
        return ""
    return reverse_str_recursive(input_str[1:])+input_str[0] ## append the first char at the last at each step and shrink
## string size by one

print(reverse_str_recursive("hello"))
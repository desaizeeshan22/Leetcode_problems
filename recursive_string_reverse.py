def reverse_str_recursive(input_str):
    if input_str=="":
        return ""
    return reverse_str_recursive(input_str[1:])+input_str[0]

print(reverse_str_recursive("hello"))
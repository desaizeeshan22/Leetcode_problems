def is_palindrome(input_str):
    if len(input_str)==0 or len(input_str)==1:
        return True
    if input_str[0]==input_str[len(input_str)-1]:
        return is_palindrome(input_str[1:len(input_str)-1])
    return False

print(is_palindrome("kayak"))
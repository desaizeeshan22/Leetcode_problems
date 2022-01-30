def palindrome_number(num):
    if num//10==0:
        return True
    result=0
    quo=num
    while quo>0:
        rem =quo%10
        quo=quo//10
        result=result*10+rem
    return num==result

print(palindrome_number(212))
print(palindrome_number(12))
print(palindrome_number(121))
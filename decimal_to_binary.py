def decimal_to_binary(num,result=0,pow=0):
    if num==0:
        return result
    result+=num%2*10**pow
    pow+=1
    return decimal_to_binary(num//2,result,pow)

print(decimal_to_binary(133))


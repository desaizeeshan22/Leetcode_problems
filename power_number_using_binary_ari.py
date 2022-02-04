##compute pow(x,n) aka x**n eg if x=2 and n=4 2**4=16
## every exponent of a number can be expressed as a product of the exponents of the number with
##multiples of 2 eg 4**5 is 4**4 x 4**1
def power(x,n):
    result=1
    while n>0:
        if n%2!=0:# if binary bit is non zero result= result*x
            result*=x
        x=x*x  ## square base at each iteration(at each step the base is equal to the square of the previous value)
        n//=2 ## popping least significant binary digit at each step to express the power n in binary form
    return result



print(power(2,4))
print(power(3,4))
def prime_factors(num):
    factors=[]
    if num<=1:
        return 
    i=2
    while i*i<=num:
        while(num%i==0):
            factors.append(i)
            num=num//i
        i+=1
    if num>1:factors.append(num)
    return factors

print(prime_factors(121))
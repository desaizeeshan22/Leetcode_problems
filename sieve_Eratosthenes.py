## Finding out prime number less than n
## Start with a boolean array marking all number as prime aka True values
## Starting from 2 if a number is prime then all it's multiples are not prime
## hence till we reach the number n we are left with True value at only the prime indices


def prime_upto_num(num):
    sieve=[True]*(num+1)
    nums=[]
    sieve[0]=sieve[1]=False
    for i in range(2,int(num**0.5+1)):
        if sieve[i]:
            j=2
            while(i*j)<=num:
                sieve[i*j]=False
                j += 1
    for i,v in enumerate(sieve):
        if v:
            nums.append(i)
    return nums

print(prime_upto_num(11))
                
                
            
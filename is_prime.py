
def is_prime(n):
    if n==2 or n==3:
        return True
    if n==1 or n%2==0 or n%3==0:
        return  False
    i=2
    while(i**2<=n):
        if(n%i==0):
            return False
        i+=1
    return True

print(is_prime(7))
print(is_prime(121))
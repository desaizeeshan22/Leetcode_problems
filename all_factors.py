def all_factors(num):
    factors=set()
    i=1
    while i**2<num:
        if num%i==0:
            factors.add(i)
        i+=1
    while i>=1:
        if num%i == 0:
            factors.add(num//i)
        i -= 1
    return factors

print(all_factors(20))
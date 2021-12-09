def recursive_summation(n):
    if n<=1:
        return n
    return n+recursive_summation(n-1)



print(recursive_summation(10))
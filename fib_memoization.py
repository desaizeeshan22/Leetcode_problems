def fib(n,memo={}):## map for memoization to lookup already calculated subproblems
    ''' main problem is to find the nth fibonacci number,
it can be broken down into adding two consecutive numbers to get next fib numbers
'''
    if n in memo:
        return memo[n]
    if n<=2:
        return 1

    else:
        value=fib(n-1,memo)+fib(n-2,memo)
        memo[n]=value
        return value

print(fib(10))
print(fib(50))
print(fib(6))
print(fib(7))



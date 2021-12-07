def fib(n):
    ''' main problem is to find the nth fibonacci number,
it can be broken down into adding two consecutive numbers to get next fib numbers
'''
    memo={}## map for memoization to lookup already calculated subproblems
    if n<=2:
        return 1
    if n in memo:
        return memo[n]
    else:
        value=fib(n-1)+fib(n-2)
        memo[n]=value
        return value

print(fib(8))



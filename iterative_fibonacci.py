def iter_fib(n):
    fib_1=1
    fib_2=1
    for i in range(2,n):
        fib_1,fib_2=fib_2,fib_1+fib_2
    return fib_2


print(iter_fib(110))
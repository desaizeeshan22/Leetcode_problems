print([0]*6)

def fib_tabulation(n):
    table=[0]*(n+1)
    table[1]=1
    for i in range(n):
        table[i+1]+=table[i]
        if (i+2)<n+1:
            table[i+2]+=table[i]
    return table[n]

print(fib_tabulation(5))
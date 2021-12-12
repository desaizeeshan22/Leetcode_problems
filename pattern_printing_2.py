"""
for an input n print n lines of the following pattern
1 2 3 4 5 .. n
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 ... n
"""

def pattern_print(n):
    if n==1:
        print(1)
        print("\n")
        return None
    for i in range(1,n+1):
        print(i,end=" ")
    print("\n")
    pattern_print(n - 1)
    for i in range(1, n + 1):
        print(i, end=" ")
    print("\n")

print(pattern_print(6))
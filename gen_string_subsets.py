result=[""]
def subsets(string,i,n,subset=[]):
    if i==n:
        return

    for j in range(i,n):
        subset.append(string[j])
        global result
        result.append("".join(subset))
        subsets(string,j+1,n,subset)
        subset.pop()
    return
n=len("ABC")
subsets("ABC",0,n)

print(result)
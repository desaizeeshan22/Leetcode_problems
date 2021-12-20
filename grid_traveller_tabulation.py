import numpy as np



def grid_traveller(m,n):
    table=np.zeros(shape=(m+1,n+1))
    table[1][1]=1
    for i in range(m+1):
        for j in range(n+1):
            current=table[i][j]
            if j+1<n+1:
                table[i][j+1]+=current
            if i+1<m+1:
                table[i+1][j]+=current
    return table[m][n]
print(grid_traveller(1,1))
print(grid_traveller(2,3))
print(grid_traveller(3,2))
print(grid_traveller(3,3))
print(grid_traveller(18,18))



def maximal_area(matrix):
    m=len(matrix)
    n=len(matrix[0])
    max_square_l=0
    for i in range(m):
        for j in range(n):
            if matrix[i][j]=="1":
                square_l=1
                flag=True
                while((i+square_l<m and j+square_l<n) and flag):
                    for k in range(i,i+square_l+1):
                        if matrix[k][j+square_l]=="0":
                            flag=False
                            break
                    for k in range(j, j + square_l + 1):
                        if matrix[i + square_l][k] == "0":
                            flag = False
                            break
                    if flag:
                        square_l+=1
                if square_l>max_square_l:
                    max_square_l=square_l
    return max_square_l*max_square_l
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# matrix=[["0","1"],["1","0"]]
print(maximal_area(matrix))
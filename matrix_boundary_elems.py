
def boundary_elems(matrix):
    if len(matrix)==0:
        return matrix
    elif len(matrix[0])==1:
        for i in range(len(matrix)):
            print(matrix[i][0])
    elif len(matrix)==1:
        for elem in matrix[-1]:
            print(elem)
    else:
        start_row=0
        end_row=len(matrix)
        start_col=0
        end_col=len(matrix[0])
        for i in range(start_col,end_col):
            print(matrix[start_row][i])
        start_row+=1
        for j in range(start_row,end_row):
            print(matrix[j][end_col-1])
        end_col-=1
        for i in range(end_col-1,start_col-1,-1):
         print(matrix[end_row-1][i])
        end_row-=1
        for j in range(end_row-1,start_row-1,-1):
            print(matrix[j][start_col])
mat=[[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12],
     [13,14,15,16]]
mat_2=[[1,2],
       [3,4],
       [5,6]]
mat_1=[[1],
       [2],
       [3],
       [4]]
boundary_elems(mat)
print("\n")
boundary_elems(mat_1)
print("\n")
boundary_elems(mat_2)


def find_elem_le(arr,target): ## function to determine the element less than or equal to target element
    lo=0
    hi=len(arr)-1
    while lo<=hi:
        mid=(lo+hi)//2
        if arr[mid]<=target:
            lo=mid+1
        else:
            hi=mid-1
    return lo

def min_row_sorted_mat(matrix):
    min_elem=float("inf")
    for i in range(len(matrix)):
        min_elem=min(min_elem,matrix[i][0])
    return min_elem
def max_row_sorted_mat(matrix):
    max_elem=float("-inf")
    for i in range(len(matrix)):
        max_elem=max(max_elem,matrix[i][-1])
    return max_elem
def median_row_sorted_array(matrix):

    n_rows=len(matrix)
    n_cols=len(matrix[0])
    lo=min_row_sorted_mat(matrix)
    hi=max_row_sorted_mat(matrix)
    while lo<=hi:
        mid=(lo+hi)//2
        count_le = 0
        for elem in matrix:
            count_le+=find_elem_le(elem,mid)
        if count_le<=((n_rows*n_cols)//2):
            lo=mid+1
        else:
            hi=mid-1
    return lo

matrix=[[1,10,20],
        [15,25,35],
        [5,30,40]]
print(median_row_sorted_array(matrix))

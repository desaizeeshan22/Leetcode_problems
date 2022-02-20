class Solution(object):
    def spiralOrder(self, matrix):
        res=[]
        if len(matrix)==0:
            return matrix
        start_row=0
        end_row=len(matrix)-1
        start_col=0
        end_col=len(matrix[0])-1
        while(start_row<=end_row and start_col<=end_col):
            i=start_col
            while i<=end_col:
                res.append(matrix[start_row][i])
                i+=1
            start_row+=1
            j=start_row
            while j<=end_row:
                res.append(matrix[j][end_col])
                j+=1
            end_col-=1
            if start_row<=end_row:
                k=end_col
                while k>=start_col:
                    res.append(matrix[end_row][k])
                    k-=1
            end_row-=1
            if start_col<=end_col:
                l=end_row
                while l>=start_row:
                    res.append(matrix[l][start_col])
                    l-=1
            start_col+=1   
        return res
            
            
                
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
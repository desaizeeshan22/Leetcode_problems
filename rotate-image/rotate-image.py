class Solution(object):
    def rotate(self, matrix):
        self.transpose(matrix)
        for elem in matrix:
            elem.reverse()
    
    def transpose(self,matrix):
        n=len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    # def reflect(self,matrix):
        
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
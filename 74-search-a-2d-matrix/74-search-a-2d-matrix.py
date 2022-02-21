class Solution(object):
    def searchMatrix(self, matrix, target):
        m=len(matrix)
        n=len(matrix[0])
        i=0
        j=n-1
        while(i<m and j>=0):
            if target==matrix[i][j]:
                return True
            elif target>matrix[i][j]:
                i+=1
            else:
                j-=1
        return False
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
class Solution(object):
    def maximalRectangle(self, matrix):
        intmat=[]
        res=[]
        for elem in matrix:
            intmat.append(map(int,elem))
        maxArea=self.maxRect(intmat[0])
        for i in range(1,len(intmat)):
            for j in range(len(intmat[0])):
                if intmat[i][j]!=0:
                    intmat[i][j]+=intmat[i-1][j]
            maxArea=max(maxArea,self.maxRect(intmat[i]))
        return maxArea
    def maxRect(self,res):
        maxArea=0
        st=[]
        st.append(-1)
        for i,v in enumerate(res):
            while(st[-1]!=-1 and res[st[-1]]>=v):
                height=res[st.pop()]
                maxArea=max((i-st[-1]-1)*height,maxArea)
            st.append(i)
        while(st[-1]!=-1):
            height=res[st.pop()]
            maxArea=max(maxArea,height*(len(res)-st[-1]-1))
        return maxArea
            
                
            
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
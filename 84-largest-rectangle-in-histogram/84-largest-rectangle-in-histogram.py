class Solution(object):
    def largestRectangleArea(self, heights):
        st=[]
        st.append(-1)
        max_area=0
        for i,v in enumerate(heights):
            while(st[-1]!= -1 and heights[st[-1]]>=v):
                curr_height=heights[st.pop()]
                curr_width=i-st[-1]-1
                max_area=max(max_area,curr_height*curr_width)
            st.append(i)
        while(st[-1]!= -1):
            height=heights[st.pop()]
            width=len(heights)-st[-1]-1
            max_area=max(max_area,height*width)
        return max_area
           
        """
        :type heights: List[int]
        :rtype: int
        """
        
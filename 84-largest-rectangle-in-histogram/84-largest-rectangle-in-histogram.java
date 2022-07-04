class Solution {
    public int largestRectangleArea(int[] heights) {
         ArrayList<Integer>nextSmall=this.nextSmaller(heights);
         ArrayList<Integer>prevSmall=this.prevSmaller(heights);
        int res=0;
         for(int i=0;i<heights.length;i++){
             int currArea=heights[i];
             currArea+=(nextSmall.get(i)-i-1)*heights[i];
             currArea+=(i-prevSmall.get(i)-1)*heights[i];
             res=Math.max(res,currArea);
         }
        return res;
        
    }
    public ArrayList<Integer>prevSmaller(int []heights){
        Stack<Integer>st=new Stack<Integer>();
        ArrayList<Integer>res=new ArrayList<Integer>();
        res.add(-1);
        st.push(0);
        for(int i=1;i<heights.length;i++){
            while(!st.isEmpty()&&heights[st.peek()]>=heights[i]){
                st.pop();
            }
            int elem=st.isEmpty()?-1:st.peek();
            st.push(i);
            res.add(elem);
        }
        return res;
    }
     public ArrayList<Integer>nextSmaller(int []heights){
        Stack<Integer>st=new Stack<Integer>();
        ArrayList<Integer>res=new ArrayList<Integer>();
        res.add(heights.length);
        st.push(heights.length-1);
        for(int i=heights.length-2;i>=0;i--){
            while(!st.isEmpty()&&heights[st.peek()]>=heights[i]){
                st.pop();
            }
            int elem=st.isEmpty()?heights.length:st.peek();
            st.push(i);
            res.add(elem);
        }
         ArrayList<Integer>fin=new ArrayList<Integer>();
          for(int j=res.size()-1;j>=0;j--){
              fin.add(res.get(j));
          }
        return fin;
    }
}
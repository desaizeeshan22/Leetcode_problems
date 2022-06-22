class StockSpanner {
    private ArrayList<Integer>stocks;
    private Stack<int[]>st;
    public StockSpanner() {
        this.stocks=new ArrayList<Integer>();
        this.st=new Stack<int[]>();
    }
    
    public int next(int price) {
        this.stocks.add(price);
        int span=1;
        while(!st.isEmpty()&&st.peek()[0]<=price){
            span+=st.peek()[1];
            st.pop();
        }
        int []temp=new int[]{price,span};
        st.push(temp);
        return span;
    }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner obj = new StockSpanner();
 * int param_1 = obj.next(price);
 */
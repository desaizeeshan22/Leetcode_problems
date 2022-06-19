class Solution {
    public boolean isValid(String s) {
        if(s.length()==1){
            return false;
        }
        Map<Character,Character>strMap=new HashMap<Character,Character>();
        Stack<Character>st=new Stack<Character>();
        strMap.put(')','(');
        strMap.put('}','{');
        strMap.put(']','[');
        for(char ch:s.toCharArray()){
            if(strMap.containsValue(ch)){
                st.push(ch);
            }
            else{
            char top=st.isEmpty()?'$':st.pop();
            if(top!=strMap.get(ch)){
                return false;
            }
            }   
        }
        return st.isEmpty();
    }
}
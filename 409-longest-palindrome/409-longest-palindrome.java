import java.util.*;
class Solution {
    public int longestPalindrome(String s) {
        Map<Character,Integer> m=new HashMap();
        for(char c:s.toCharArray()){
            if(m.containsKey(c)){
                Integer old_count=(int)m.get(c);
                m.put(c,old_count+1);
            }
            else{
                m.put(c,1);
            }
        }
        int res=0;
        for(Map.Entry elem:m.entrySet()){
            int v=(int)elem.getValue();
            res+=(v/2)*2;
            if(res%2==0 && v%2==1){
                res+=1;
            }
        }
        return res;
    }
}
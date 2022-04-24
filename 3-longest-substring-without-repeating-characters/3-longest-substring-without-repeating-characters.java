class Solution {
    public int lengthOfLongestSubstring(String s) {
        if(s==""){
            return 0;
        }
        int res=0;
         Map<Character,Integer>hashMap=new HashMap<Character,Integer>();
        int left=0;
        for(int right=0;right<s.length();right++){
            if(hashMap.containsKey(s.charAt(right))){
                left=Math.max(left,hashMap.get(s.charAt(right))+1);
            }
            hashMap.put(s.charAt(right),right);
             res=Math.max(res,right-left+1);
        }
        return res;
        
    }
}
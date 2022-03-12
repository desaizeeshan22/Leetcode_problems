class Solution {
    public int firstUniqChar(String s) {
        int res[]=new int[26];
        Arrays.fill(res,0);
        for(int i=0;i<s.length();i++){
            res[(int)s.charAt(i)-'a']++;
        }
        int index=-1;
        for(int i=0;i<s.length();i++){
            if(res[(int)s.charAt(i)-'a']==1){
                index=i;
                break;
            }
        } 
        return index;
    }
}
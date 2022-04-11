class Solution {
    public boolean rotateString(String s, String goal) {
        if(s.length()!=goal.length()){
            return false;
        }
        String s_concat=s+s;
        for(int i=0;i<(s_concat.length()-goal.length()+1);i++){
            int j=0;
            for(;j<goal.length();j++){
                if(goal.charAt(j)!=s_concat.charAt(i+j)){
                    break;
                }
            }
            if(j==goal.length()){
                return true;
            }
        }
        return false;
    }
}
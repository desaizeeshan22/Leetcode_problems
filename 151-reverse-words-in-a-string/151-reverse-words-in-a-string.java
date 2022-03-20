import java.util.Collections;
class Solution {
    public void reverse(char[] c,int st,int end){
            while(st<=end){
                char temp=c[st];
                c[st]=c[end];
                c[end]=temp;
                st++;
                end--;
            }
        }
    public StringBuilder rem_spaces(char[] t){
        StringBuilder sb = new StringBuilder();
        int left=0;
        while(t[left]==' '){
            left++;
        }
        int right=t.length-1;
        while(t[right]==' '){
            right--;
        }
        for(int i=left;i<=right;i++){
            if(t[i]!=' '){
                sb.append(t[i]);
            }
            else if(t[i]==' ' &&t[i-1]!=' '){
                sb.append(t[i]);
            }
        }
        return sb;
    }
    public String reverseWords(String s) {
        int j=0;
        int i=0;
        char[]c=s.toCharArray();
        while(j<c.length){
            if(c[j]==' '){
                reverse(c,i,j-1);
                i=j+1  ; 
            }
            j++;
        }
        reverse(c,i,c.length-1);
        reverse(c,0,c.length-1);
        StringBuilder sb=rem_spaces(c);
        return sb.toString();
        }
    }

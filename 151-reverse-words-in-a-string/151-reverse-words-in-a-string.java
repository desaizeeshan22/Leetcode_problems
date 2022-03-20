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
        for(int i=0;i<t.length;i++){
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
        String t=s.trim();
        char[]c=t.toCharArray();
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

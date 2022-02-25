class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer>s1=new HashSet<Integer>();
        Set<Integer>s2=new HashSet<Integer>();
        for (int elem:nums1){s1.add(elem);}
        
        for(int elem:nums2){
            if(s1.contains(elem)){
                s2.add(elem);
            }
        }
        int i=0;
        int[]res=new int[s2.size()];
        for (int elem:s2){res[i++]=elem;}
        return res;
    }
}
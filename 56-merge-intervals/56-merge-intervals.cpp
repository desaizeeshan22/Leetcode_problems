class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> res;
      
        sort(intervals.begin(),intervals.end(),[ ]( const auto& lhs, const auto& rhs ){
   return lhs[0] < rhs[0];});
       for(auto elem:intervals){
           if (res.empty() || res.back()[1]<elem[0]){
               res.push_back(elem);
           }
           else{
               res.back()[1]=max(elem[1],res.back()[1]);
           }
       }
        return res;
    }
};
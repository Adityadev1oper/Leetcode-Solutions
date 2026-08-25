class Solution {
public:
    int missingMultiple(vector<int>& nums, int k) {
        set<int>s;
        for(int num : nums){
            s.insert(num);
        }
        int multiple = k;

        while(s.find(multiple) != s.end()){
            multiple += k;
        }

        return multiple;

        
    }
};
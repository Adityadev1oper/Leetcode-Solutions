class Solution {
public:
    int smallestIndex(vector<int>& nums) {
        int i = 0;
        while(i <nums.size()){
            int sum = 0 ;
            while(nums[i] != 0){
                
                sum += nums[i] % 10;
                nums[i] = nums[i]/10; 

            }
            if(sum == i){
                return i;
            }else{
                i++;
            }

        }
        return -1;
    }
};
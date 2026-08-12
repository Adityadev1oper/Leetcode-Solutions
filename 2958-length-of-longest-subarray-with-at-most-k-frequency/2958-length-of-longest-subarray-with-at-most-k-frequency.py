class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mp = {}
        i , j = 0,0 
        result = 0 
        while (j < n) :
            mp[nums[j]] =  mp.get(nums[j],0) + 1
            while (mp[nums[j]] > k ):
                mp[nums[i]] -= 1 
                i+= 1 
            result = max(result,j-i+1)
            j+= 1
        return result
        
        
                
            


        
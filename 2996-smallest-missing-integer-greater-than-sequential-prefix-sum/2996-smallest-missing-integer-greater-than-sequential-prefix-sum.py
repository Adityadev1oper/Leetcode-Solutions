class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        hashset = set(nums) 
        totalSum = nums[0]

        for j in range(1,len(nums)):
            if nums[j] == nums[j-1] +1:
                totalSum += nums[j]
            else: 
                break
        
        while totalSum in hashset:
            totalSum+= 1

        return totalSum  
        
        
        
                

        

            
        

            


            
        
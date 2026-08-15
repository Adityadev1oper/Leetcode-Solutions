class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xr = 0
        zero = 0

        for x in nums:
            xr ^= x
            if x == 0:
                zero += 1

        if xr != 0:
            return len(nums)

        return 0 if zero == len(nums) else len(nums) - 1
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        ans = []

        if len(set1) > len(set2):
            for hash in set2:
                if hash in set1:
                    ans.append(hash)
        else:
            for hash in set1:
                if hash in set2:
                    ans.append(hash)
        return ans

                    

        
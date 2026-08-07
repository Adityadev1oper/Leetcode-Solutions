from typing import List

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:

        def units_removed(time, w):
            low, high = 0, mountainHeight
            while low <= high:
                mid = (low + high) // 2
                if w * mid * (mid + 1) // 2 <= time:
                    low = mid + 1
                else:
                    high = mid - 1
            return high

        def can_finish(time):
            removed = 0
            for w in workerTimes:
                removed += units_removed(time, w)
                if removed >= mountainHeight:
                    return True
            return False

        left = 0
        right = min(workerTimes) * mountainHeight * (mountainHeight + 1) // 2

        while left < right:
            mid = (left + right) // 2
            if can_finish(mid):
                right = mid
            else:
                left = mid + 1

        return left
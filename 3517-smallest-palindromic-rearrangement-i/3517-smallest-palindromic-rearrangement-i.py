class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        hashmap = {}

        for ch in s:
            hashmap[ch] = hashmap.get(ch, 0) + 1

        sorted_freq = dict(sorted(hashmap.items()))

        ans = [''] * len(s)

        left = 0
        right = len(s) - 1

        for ch in sorted_freq:
            while sorted_freq[ch] >= 2:
                ans[left] = ch
                ans[right] = ch
                sorted_freq[ch] -= 2
                left += 1
                right -= 1

        for ch in sorted_freq:
            if sorted_freq[ch] == 1:
                ans[left] = ch
                break

        return "".join(ans)
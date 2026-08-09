class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1

        # Skip trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1

        # Count the last word
        count = 0
        while i >= 0 and s[i] != ' ':
            count += 1
            i -= 1

        return count
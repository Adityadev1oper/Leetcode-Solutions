class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        while True:
            num = n          
            pro = 1         

            while num > 0:
                pro *= (num % 10)
                num //= 10

            if pro % t == 0:
                return n

            n += 1
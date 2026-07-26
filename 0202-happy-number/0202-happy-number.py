class Solution:
    def isHappy(self, n: int) -> bool:

        hi = set()

        while n != 1:

            if n in hi:
                return False

            hi.add(n)

            n = self.hola(n)

        return True

    def hola(self, n):

        total = 0

        while n > 0:
            digit = n % 10
            total += digit * digit
            n //= 10

        return total
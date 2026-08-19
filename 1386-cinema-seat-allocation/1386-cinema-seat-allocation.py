from collections import defaultdict
from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = defaultdict(int)
        for r, c in reservedSeats:
            if 2 <= c <= 9:
                rows[r] |= 1 << (c - 2)   # bits 0..7 represent seats 2..9

        LEFT  = 0b00001111   # seats 2-5
        MID   = 0b00111100   # seats 4-7
        RIGHT = 0b11110000   # seats 6-9

        # rows with no reservations at all: 2 families each
        total = 2 * (n - len(rows))

        for mask in rows.values():
            if (mask & LEFT) == 0 and (mask & RIGHT) == 0:
                total += 2
            elif (mask & LEFT) == 0 or (mask & RIGHT) == 0 or (mask & MID) == 0:
                total += 1

        return total
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for _ in range(32):
            bit = 1 & n
            res = (res << 1) | bit
            n >>= 1

        return res
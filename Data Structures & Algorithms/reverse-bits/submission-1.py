class Solution:
    def reverseBits(self, n: int) -> int:
        # Every loop
        ## 1.Take last bit of n
        ## 2. Shift result left
        ## 3. Add bit
        ## 4. Shift n right

        result = 0
        for _ in range(32):
            bit = n & 1
            result = (result << 1) | bit
            n >>= 1

        return result
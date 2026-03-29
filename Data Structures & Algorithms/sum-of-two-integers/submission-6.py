class Solution:
    def getSum(self, a: int, b: int) -> int:
        # a ^ b gives the sum without the carry
        # (a & b) << 1 computes the carry

        # For negative numbers, python uses an infinite length binary representation
        ## need to simulate 32 bit system with a mask

        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b != 0:
            carry = (a & b) << 1    # acts like adding then shifting bits to represent carry
            ## eg. (01 + 01) << 1 aka 1+1   
            ##      = 01 << 1 = 010 aka 2
            a = (a ^ b) & mask
            b = carry & mask    
            # when the carry is 0, it means a represents the sum value

        return a if a <= max_int else ~(a ^ mask)
        # a > max_int means need to convert from 2's complement to Python integer
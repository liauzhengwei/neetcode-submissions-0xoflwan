class Solution:
    def reverse(self, x: int) -> int:
        res = 0

        while x != 0:
            digit = (x % 10)

            if x < 0 and digit > 0:
                digit -= 10

            x = int(x / 10)

            if res < (-2**31 - 1) // 10 or res > (2**31 -1) // 10:
                return 0

            res = res * 10 + digit

        return res
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = "".join(char.lower() for char in s if char.isalnum())

        length = len(newS)
        left = 0
        right = length - 1
        while left < right:
            if newS[left] == newS[right]:
                left += 1
                right -= 1
            else:
                return False

        return True
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanS = re.sub('[^A-Za-z0-9]','', s.lower())

        left = 0
        right = len(cleanS) - 1

        while left <= right:
            if cleanS[left] != cleanS[right]:
                return False

            left += 1
            right -= 1

        return True

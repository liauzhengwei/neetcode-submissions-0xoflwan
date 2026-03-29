class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0

        cleanS = re.sub('[^0-9A-Za-z]','',s.lower())
        right = len(cleanS) - 1

        while left <= right:
            if cleanS[left] != cleanS[right]:
                return False
            
            left += 1
            right -= 1

        return True
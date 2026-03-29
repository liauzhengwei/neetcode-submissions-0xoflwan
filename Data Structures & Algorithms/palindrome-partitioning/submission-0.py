class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def backtrack(start, path):
            # Base case: if reached end of string
            if start == len(s):
                result.append(path[:])
                return

            for end in range(start + 1, len(s) + 1):
                # Get current substring
                substring = s[start:end]

                # Only proceed if substring is a palindrome                
                if ispalindrome(substring):
                    path.append(substring)
                    backtrack(end, path)
                    path.pop()

        def ispalindrome(text):
            if len(text) == 1:
                return True

            right = len(text) - 1
            left = 0

            while left < right:
                if text[left] == text[right]:
                    left += 1
                    right -= 1
                else:
                    return False

            return True


        result = []
        backtrack(0,[])
        return result
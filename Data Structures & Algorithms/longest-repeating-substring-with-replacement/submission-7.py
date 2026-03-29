class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxLength = 0
        char_count = {}
        maxFreq = 0

        for right in range(len(s)):
            char_count[s[right]] = char_count.get(s[right], 0) + 1

            maxFreq = max(maxFreq, char_count[s[right]])

            while (right - left + 1) - maxFreq > k:
                char_count[s[left]] -= 1
                left += 1
            
            maxLength = max(maxLength, right - left + 1)

        return maxLength
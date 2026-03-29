class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        max_count = 0
        left = 0
        max_length = 0

        for right in range(len(s)):
            count[s[right]] += 1 # Increment count of current character
            max_count = max(max_count, count[s[right]]) # Find the max count of any character
            
            # window size is right - left + 1
            # If more than k characters need to be replaced, shrink the window
            if(right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length

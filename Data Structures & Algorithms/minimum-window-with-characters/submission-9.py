class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_len = float('inf')
        min_left = 0

        left = 0

        t_count = {}
        window_count = {}

        for i in range(len(t)):
            t_count[t[i]] = t_count.get(t[i], 0) + 1

        formed = 0
        required = len(t_count)

        for right in range(len(s)):
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1

            if char in t_count and t_count[char] == window_count[char]:
                formed += 1

            while left <= right and formed == required:
                char = s[left]
                
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_left = left

                window_count[char] -= 1
                left += 1

                if char in t_count and window_count[char] < t_count[char]:
                    formed -= 1
        
        return "" if min_len == float('inf') else s[min_left:min_left + min_len]
                
        
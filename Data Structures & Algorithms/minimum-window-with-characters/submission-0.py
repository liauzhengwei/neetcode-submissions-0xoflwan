class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_length = float('inf')
        countT = defaultdict(int)
        countS = defaultdict(int)
        left = 0
        have = 0
        fin_start = 0
        fin_end = 0

        for c in t:
            countT[c] += 1

        need = len(countT)


        for right in range(len(s)):
            countS[s[right]] += 1

            if s[right] in countT and countT[s[right]] == countS[s[right]]:
                have += 1

            while have == need:
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    fin_start = left
                    fin_end = right

                countS[s[left]] -= 1
                if s[left] in countT and countS[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1

        return s[fin_start:fin_end+1] if min_length != float('inf') else ""
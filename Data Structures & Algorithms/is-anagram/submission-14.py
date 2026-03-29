class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        countT = {}

        for ch in s:
            if ch not in countS:
                countS[ch] = 1
            else:
                countS[ch] += 1

        for ch in t:
            if ch not in countT:
                countT[ch] = 1
            else:
                countT[ch] += 1
         
        return countT == countS
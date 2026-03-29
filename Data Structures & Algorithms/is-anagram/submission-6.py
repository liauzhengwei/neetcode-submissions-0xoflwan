class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countT = {}
        countS = {}

        for i in t:
            countT[i] = countT.get(i, 0) + 1

        for j in s:
            countS[j] = countS.get(j, 0) + 1

        return countS == countT
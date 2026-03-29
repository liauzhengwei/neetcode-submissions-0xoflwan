class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sortS = sorted(s)
        sortT = sorted(t)

        for i in range(len(s)):
            if sortS[i] != sortT[i]:
                return False

        return True
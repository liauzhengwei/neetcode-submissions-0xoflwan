class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 or not s2 or len(s2) < len(s1):
            return False

        s1_count = Counter(s1)
        window_size = len(s1)

        for i in range(len(s2) - window_size + 1):
            window = s2[i : i + window_size]

            if Counter(window) == s1_count:
                return True

        return False



        

        
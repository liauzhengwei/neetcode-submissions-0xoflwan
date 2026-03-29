class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = defaultdict(int)
        count2 = defaultdict(int)
        left = 0
        
        if len(s1) > len(s2):
            return False   

        # window size of s2 is the length of s2
        for right1 in range(len(s1)):
            count1[s1[right1]] += 1

        for right2 in range(len(s2)):
            count2[s2[right2]] += 1
            if (right2 - left + 1) > len(s1):
                count2[s2[left]] -= 1
                if count2[s2[left]]==0:
                    del count2[s2[left]]
                left += 1

            if count1 == count2:
                return True
        
        return False


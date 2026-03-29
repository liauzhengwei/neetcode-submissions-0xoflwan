class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)

        for strin in strs:
            key = tuple(sorted(strin))
            anagram[key].append(strin)

        return list(anagram.values())
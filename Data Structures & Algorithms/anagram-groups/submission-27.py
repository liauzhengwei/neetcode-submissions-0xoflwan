class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for strin in strs:
            key = tuple(sorted(strin))
            anagrams[key].append(strin)

        return list(anagrams.values())
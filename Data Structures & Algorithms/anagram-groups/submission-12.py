class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)

        # sorted() returns a list
        for strin in strs:
            key = tuple(sorted(strin))
            anagram[key].append(strin)

        return list(anagram.values())

class Solution:

    def encode(self, strs: List[str]) -> str:
        # join should apply to all the strings in strs
        # use {} when f""" is used
        return ''.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            # remember to change the value to integer
            length = int(s[i:j])
            j += 1
            res.append(s[j:j+length])
            # update the position of the index after every word
            i = j + length

        return res

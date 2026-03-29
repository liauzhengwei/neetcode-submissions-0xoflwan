class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPal(sub):
            return sub == sub[::-1]

        def bt(start, current):
            if start == len(s):
                res.append(current[:]) 
                return

            for end in range(start + 1, len(s) + 1):
                substr = s[start:end]
                if isPal(substr):
                    current.append(substr)
                    bt(end, current)
                    current.pop()

        bt(0, [])
        return res

            
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalin(sub):
            return sub == sub[::-1]

        def backtrack(start, current):
            if start == len(s):
                res.append(current[:])
                return

            for end in range(start + 1, len(s) + 1):
                substr = s[start:end]
                if isPalin(substr):
                    current.append(substr)
                    backtrack(end, current)
                    current.pop()


        backtrack(0, [])
        return res
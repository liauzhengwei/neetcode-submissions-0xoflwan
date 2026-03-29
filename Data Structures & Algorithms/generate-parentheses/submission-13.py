class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def bt(current, open_count, close_count):
            if len(current) == 2 * n:
                res.append(current)
                return

            if open_count < n:
                bt(current + "(", open_count + 1, close_count)

            if close_count < open_count:
                bt(current + ")", open_count, close_count + 1)

        bt("",0,0)
        return res
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(current, open_count, close_count):
            if len(current) == n * 2:
                res.append(current)
                return

            if open_count < n:
                dfs(current + "(", open_count + 1, close_count)

            if close_count < open_count:
                dfs(current + ")", open_count, close_count + 1)

        dfs("", 0,0)
        return res

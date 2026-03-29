class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(start, current, remain):
            if remain == 0:
                res.append(current[:])
                return
            
            if remain < 0:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                if remain < candidates[i]:
                    break

                current.append(candidates[i])
                backtrack(i + 1, current, remain - candidates[i])
                current.pop()

        backtrack(0, [], target)
        return res







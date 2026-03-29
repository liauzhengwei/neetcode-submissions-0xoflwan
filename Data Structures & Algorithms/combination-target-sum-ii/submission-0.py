class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)

        def backtrack(start, path, current_sum):
            if current_sum == target:
                result.append(path[:])
                return  # return added to stop further exploration
            
            if current_sum > target:
                return

            for i in range(start, len(candidates)):
                # Skip duplicates: if current element is same as previous, skip
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                # add candidates to the path 
                path.append(candidates[i])

                # recursive function
                backtrack(i+1, path, current_sum + candidates[i])

                # Backtrack
                path.pop()



        result = []
        backtrack(0,[],0)
        return result
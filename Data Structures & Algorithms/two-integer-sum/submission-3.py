class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}

        for i, num in enumerate(nums):
            difference = target - num
            if difference in index_map: # meaning the 'difference' key exists, can obtain the index
                return [index_map[difference], i]
            
            index_map[num] = i  # else add the current number as key and assign the index as the value

        return []

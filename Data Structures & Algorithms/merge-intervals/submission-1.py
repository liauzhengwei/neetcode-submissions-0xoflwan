class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])

        temp = intervals[0]
        result = []

        for interval in intervals[1:]:
            if interval[0] <= temp[1]:
                temp[1] = max(temp[1], interval[1])
            else:
                result.append(temp)
                temp = interval

        result.append(temp)
        return result
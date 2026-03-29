class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = []
        self.timemap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
        
        result = ""
        values = self.timemap[key]

        left = 0
        right = len(values) - 1

        while left <= right:
            mid = (left + right)//2
            mid_mood , mid_time = values[mid]

            if mid_time == timestamp:
                return mid_mood
            elif mid_time < timestamp:
                result = mid_mood
                left = mid + 1
            else:
                right = mid - 1

        return result
class TimeMap:

    def __init__(self):
             self.timeMap = {}
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.timeMap:
            return ""

        values = self.timeMap[key]
        
        left = 0
        right = len(values) - 1
        ans = ""
        while (left <= right):
            mid = left + (right - left) // 2

            mid_value, mid_time = values[mid]
            if mid_time <= timestamp:
                ans = mid_value
                left = mid +   1
            else:
                right = mid - 1
        return ans
            
from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.hashMap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashMap[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        value = self.hashMap[key]
        left, right = 0, len(value) - 1
        key = ""

        while left <= right:
            mid = left + (right - left) // 2
            if value[mid][0] <= timestamp:
                key = value[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return key
        

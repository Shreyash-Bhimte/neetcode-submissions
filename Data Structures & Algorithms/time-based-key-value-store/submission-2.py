class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data.setdefault(key,[]).append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.data:
            return ""
    
        left = 0
        right = len(self.data[key]) - 1

        while left <= right:
            mid = (left + right) // 2

            if self.data[key][mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid - 1

        if left > 0:
            return self.data[key][left - 1][1]
        return ""
class TimeMap:

    def __init__(self):
        self.store: Dict[str, Dict[int, str]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key]: Dict[int, str] = {}
        self.store[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        timestamps = list(self.store[key].keys())

        if not timestamps or (timestamps and timestamp<timestamps[0]):
            return ""

        l, r = 0, len(timestamps)-1

        while l<=r:
            mid = l + ((r-l)//2)

            if timestamps[mid] == timestamp:
                return self.store[key][timestamp]
            elif timestamp < timestamps[mid]:
                r = mid - 1
            else:
                l = mid + 1
        
        return self.store[key][timestamps[r]]

        

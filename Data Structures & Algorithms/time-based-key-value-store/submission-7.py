class TimeMap:

    def __init__(self):
        self.key_store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_store:
            self.key_store[key] = {}

        self.key_store[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_store:
            return ""
        
        values = list(self.key_store[key].keys())
        l, r, res = 0, len(values)-1, ""

        while l<=r:
            mid = l + ((r-l)//2)
            if values[mid] <= timestamp:
                res = self.key_store[key][values[mid]]
                l = mid + 1
            else:
                r = mid - 1
        
        return res
        

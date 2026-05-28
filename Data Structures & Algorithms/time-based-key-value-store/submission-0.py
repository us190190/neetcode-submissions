class TimeMap:

    def __init__(self):
        self.key_store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_store:
            self.key_store[key] = []
        self.key_store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:

        values = self.key_store[key] if key in self.key_store else []
        res = ""
        l, r = 0, len(values)-1

        while l<=r:
            mid = l+((r-l)//2)
            if values[mid][0]==timestamp:
                res = values[mid][1]
                break
            elif timestamp<values[mid][0]:
                r = mid-1
            else:
                l = mid+1
                res = values[mid][1]
        
        return res





        

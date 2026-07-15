class MedianFinder:

    def __init__(self):
        self.max_lh = []
        self.min_rh = []

    def addNum(self, num: int) -> None:
        len_lh = len(self.max_lh)
        len_rh = len(self.min_rh)
        if len_lh<=len_rh:
            if len_rh:
                right = heapq.heappop(self.min_rh)
                if num<right:
                    heapq.heappush(self.max_lh, -num)
                    heapq.heappush(self.min_rh, right)
                else:
                    heapq.heappush(self.max_lh, -right)
                    heapq.heappush(self.min_rh, num)
            else:
                heapq.heappush(self.max_lh, -num)
        else:
            if len_lh:
                left = -heapq.heappop(self.max_lh)
                if num>left:
                    heapq.heappush(self.min_rh, num)
                    heapq.heappush(self.max_lh, -left)
                else:
                    heapq.heappush(self.min_rh, left)
                    heapq.heappush(self.max_lh, -num)
            else:
                heapq.heappush(self.min_rh, num)

    def findMedian(self) -> float:
        len_lh = len(self.max_lh)
        len_rh = len(self.min_rh)

        if len_lh == len_rh:
            return (-self.max_lh[0] + self.min_rh[0])/2
        elif len_lh>len_rh:
            return -self.max_lh[0]
        else:
            return self.min_rh

        
        
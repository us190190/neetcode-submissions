class MedianFinder:

    def __init__(self):

        # [1,2,3,4,5,6,7] [8,9,10,11,12,13]

        self.max_h = []
        self.min_h = []

    def addNum(self, num: int) -> None:

        left = self.max_h[0] if len(self.max_h) else float('-inf')
        right = self.min_h[0] if len(self.min_h) else float('inf')

        if num <= right:
            # put in left heap
            heapq.heappush(self.max_h, -num)
            # balance
            if (len(self.max_h)-len(self.min_h))>1:
                popped = heapq.heappop(self.max_h)
                heapq.heappush(self.min_h, -popped)
        else:
            # put in right heap
            heapq.heappush(self.min_h, num)
            # balance
            if (len(self.min_h)-len(self.max_h))>1:
                popped = heapq.heappop(self.min_h)
                heapq.heappush(self.max_h, -popped)

    def findMedian(self) -> float:

        len_left = len(self.max_h)
        len_right = len(self.min_h)

        if len_left == len_right:
            return (-self.max_h[0] + self.min_h[0])/2
        elif len_left>len_right:
            return -self.max_h[0]
        else:
            return self.min_h[0]


        
        
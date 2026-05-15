class MedianFinder:

    def __init__(self):
        self.left_max_heap = []
        self.right_min_heap = []

    def addNum(self, num: int) -> None:
        lh_len = len(self.left_max_heap)
        rh_len = len(self.right_min_heap)
        if lh_len <= rh_len:
            if len(self.right_min_heap):
                right_popped = heapq.heappop(self.right_min_heap)
                if num>right_popped:
                    heapq.heappush(self.left_max_heap, -1*right_popped)
                    heapq.heappush(self.right_min_heap, num)
                else:
                    heapq.heappush(self.left_max_heap, -1*num)
                    heapq.heappush(self.right_min_heap, right_popped)
            else:
                heapq.heappush(self.left_max_heap, -1*num)
        else:
            if len(self.left_max_heap):
                left_popped = -1*heapq.heappop(self.left_max_heap)
                if num<left_popped:
                    heapq.heappush(self.left_max_heap, -1*num)
                    heapq.heappush(self.right_min_heap, left_popped)
                else:
                    heapq.heappush(self.left_max_heap, -1*left_popped)
                    heapq.heappush(self.right_min_heap, num)
            else:
                heapq.heappush(self.right_min_heap, num)

    def findMedian(self) -> float:
        lh_len = len(self.left_max_heap)
        rh_len = len(self.right_min_heap)

        result = 0
        if lh_len < rh_len:
            result = heapq.heappop(self.right_min_heap)
            heapq.heappush(self.right_min_heap, result)
        elif lh_len > rh_len:
            result = -1*heapq.heappop(self.left_max_heap)
            heapq.heappush(self.left_max_heap, -1*result)
        else:
            left = -1*heapq.heappop(self.left_max_heap)
            heapq.heappush(self.left_max_heap, -1*left)
            right = heapq.heappop(self.right_min_heap)
            heapq.heappush(self.right_min_heap, right)
            result = (left+right)/2
        return result
        
        
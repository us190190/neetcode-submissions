class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        ref = {}

        for task in tasks:
            if task not in ref:
                ref[task] = 0
            ref[task] += 1
        
        max_h = []
        for key,val in ref.items():
            heapq.heappush(max_h, -val)
        
        time = 0
        cooldown_q = deque()
        while max_h or cooldown_q:
            # print(f"max_h: {max_h} cooldown_q: {cooldown_q}")
            time += 1
            if max_h:
                tsk = heapq.heappop(max_h)
                tsk += 1
                if tsk:
                    cooldown_q.append([tsk, time+n])
            # else:
            #     time = cooldown_q[0][1]
            if cooldown_q and cooldown_q[0][1]==time:
                heapq.heappush(max_h, cooldown_q.popleft()[0])
        
        return time







        
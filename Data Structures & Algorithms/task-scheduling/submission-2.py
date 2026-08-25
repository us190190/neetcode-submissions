class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        ref = defaultdict(int) # remaining frequency of each task
        pending = [] # priorty of remaining task
        clock = 1

        for task in tasks:
            ref[task] += 1

        for task, f in ref.items():
            heapq.heappush(pending, -f)
        
        time = 0
        cooldown_q = deque()

        while cooldown_q or pending:
            time += 1
            if pending:
                tsk = heapq.heappop(pending)
                tsk += 1
                if tsk:
                    cooldown_q.append([tsk, time+n])
            else:
                time = cooldown_q[0][1]
            if cooldown_q and time == cooldown_q[0][1]:
                heapq.heappush(pending, cooldown_q.popleft()[0])
        
        return time


            
            




        
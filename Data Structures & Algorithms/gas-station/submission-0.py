class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas)<sum(cost):
            return -1
        needs = []

        for i in range(len(gas)):
            needs.append(gas[i]-cost[i])
        
        idx, seen, s = 0, 0, 0
        while seen<len(needs):

            s += needs[idx]
            seen += 1
            if seen==len(needs):
                return (idx+1)%(len(needs))
            if s<=0:
                s = 0
                seen = 0
            
            idx = (idx+1)%(len(needs))



        

        
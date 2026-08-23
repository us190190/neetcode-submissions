class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = []

        for i in range(len(position)):
            time_taken = (target-position[i])/speed[i]
            cars.append((position[i], time_taken))

        cars.sort(reverse=True)

        # print(cars)
        stk = []

        # C1________C2_______C3______C4____________D

        for car_postion, car_time in cars:
            if (not stk) or (stk and stk[-1][1]<car_time):
                stk.append((car_postion, car_time))
        
        return len(stk)





        
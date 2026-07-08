class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:


        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        
        cars.sort()
        stk = []

        for i in range(len(cars)-1, -1, -1):
            car = cars[i]
            car_time = (target-car[0])/car[1]
            if stk:
                ahead_car = stk[-1]
                ahead_time = (target-ahead_car[0])/ahead_car[1]
                if car_time<=ahead_time:
                    continue
            stk.append(car)
        return len(stk)
        
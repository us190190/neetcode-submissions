class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        result, cars = [], []

        length = len(position)

        cars = []

        for i, pos in enumerate(position):
            cars.append((pos, speed[i]))

        s_cars = sorted(cars)

        while s_cars:
            current_car = s_cars.pop()
            t = (target - current_car[0]) / current_car[1]
            if (not result) or (result and t>result[-1]):
                result.append(t)
        
        return len(result)
            




        
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = []
        result = []

        for idx in range(len(position)):
            cars.append((position[idx], speed[idx]))
        
        cars.sort()
        result.append(cars.pop())

        while cars:
            c_car = cars.pop()
            time_c_car = (target-c_car[0]) / c_car[1]
            t_car = result[-1]
            time_t_car = (target-t_car[0]) / t_car[1]
            if time_c_car > time_t_car:
                result.append(c_car)
        
        return len(result)

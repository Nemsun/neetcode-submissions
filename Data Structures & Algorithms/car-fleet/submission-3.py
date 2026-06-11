class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p,(target - p) / s) for p,s in zip(position, speed)]
        cars.sort(reverse=True)

        car_fleets = 0
        max_time = 0
        for _, time in cars:
            if time > max_time:
                car_fleets += 1
                max_time = time
        return car_fleets
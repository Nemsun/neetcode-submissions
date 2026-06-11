class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # keep track of the position and the time it takes for them to reach the destination
        cars = [(p, (target - p) / s) for p, s in zip(position, speed)]
        
        # reverse sort to track the farthest car
        cars.sort(reverse=True)

        # keep track of the time it takes
        # basically same time == fleet
        fleets = 0
        max_time = 0

        for _, time in cars:
            if time > max_time:
                fleets += 1
                # new fleet
                max_time = time
        return fleets
'''
There are n cars traveling to the same destination on a one-lane highway.

- n cars, 1 <= n <= 1000

You are given two arrays of integers position and speed, both of length n.

- two arrays, position and speed of cars

position[i] is the position of the ith car (in miles)
speed[i] is the speed of the ith car (in miles per hour)

- speed and position are directly associated with the car

The destination is at position target miles.

- target is the goal

A car can not pass another car ahead of it. 
It can only catch up to another car and then drive at the same speed as the car ahead of it.

- positions can't change, only speed can

A car fleet is a non-empty set of cars driving at the same position and same speed. 
A single car is also considered a car fleet.

- a car fleet exists if and only if cars are at the same position and speed
- each single car is considered its own fleet

If a car catches up to a car fleet the moment the fleet reaches the destination, 
then the car is considered to be part of the fleet.

- before we reach the target, if the car has the same position and speed -> add to fleet

Return the number of different car fleets that will arrive at the destination.
- combinatorics? maybe?


example:

Input: target = 10, position = [1,4], speed = [3,2]

Output: 1

target = 10
car 1: position 1, speed 3 -> position 4 -> position 7 -> position 10
car 2: position 4, speed 2 -> position 6 -> position 8 -> position 10

we meet at 10, so car fleet = 1
'''

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = [[p, s] for p, s in zip(position, speed)]
        car.sort(reverse=True)
        stack = []
        for p, s in car:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
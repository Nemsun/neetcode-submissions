'''
You are given an array of integers temperatures 
where temperatures[i] represents the daily temperatures on the ith day.

- list of temperatures
- each index is the daily temperature


Return an array result where result[i] is the number of days after the ith day 
before a warmer temperature appears on a future day. If there is no day 
in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.

- result[i] is # of days AFTER the ith day before a warmer temperature appears


example:

Input: temperatures = [30,38,30,36,35,40,28]

30 -> 38 [1]
38 -> 30 [1] -> 36 [2] -> 35 [3] -> 40 [4]

rules:
- we look at the current element as the base line so we need a loop
- check each subsequent element if base case > next case, then stop, else increment and continue

'''



class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # pair [temp, ind]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackTemp, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t, i])
        return res
                    
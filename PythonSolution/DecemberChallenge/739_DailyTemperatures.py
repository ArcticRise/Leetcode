"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

"""
from typing import List

def dailyTemperatures(temperatures: List[int]) -> List[int]:
    stack=[]
    ans=[0]*len(temperatures)
    for ind,temp in enumerate(temperatures):
        while stack and temp > stack[-1][1]:
            i,t = stack.pop()
            ans[i]=ind-i
        stack.append((ind,temp))
    return ans

temperatures = [73,74,75,71,69,72,76,73]
print(dailyTemperatures(temperatures))

"""

Time/Space : O(N)

"""
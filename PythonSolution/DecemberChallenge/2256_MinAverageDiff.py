"""
The average difference of the index i is the absolute difference between the average of the first i + 1 elements of nums and the average of the last n - i - 1 elements. Both averages should be rounded down to the nearest integer.

Return the index with the minimum average difference. If there are multiple such indices, return the smallest one.

Note:

The absolute difference of two numbers is the absolute value of their difference.
The average of n elements is the sum of the n elements divided (integer division) by n.
The average of 0 elements is considered to be 0.

input: [2,5,3,9,5,3]
output: 3


"""
from typing import List

def minimumAverageDifference(nums: List[int]) -> int:
    sum_arr = []
    #Go Through get the sum at each index
    running_total = 0
    for n in nums:
        running_total += n
        sum_arr.append(running_total)
    
    
    #Now Loop through sum_arr to get the abs of all
    ans = []
    for n in range(len(sum_arr)):
        val1 = (sum_arr[n]//(n+1))
        val2 = (sum_arr[-1]-sum_arr[n])
        #Doing this to Avoid Div by Zero
        div = ((len(sum_arr)-n)-1) if ((len(sum_arr)-n)-1) > 0 else 1
        total = val1 - val2//div
        ans.append(abs(total))
    return ans.index(min(ans))


Case1 = [2,5,3,9,5,3]
print(minimumAverageDifference(Case1))

"""
Time Complexity: O(N)
Space Complexity O(N)

"""
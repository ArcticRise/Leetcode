"""
Given an Array Replace every Elem with the greatest right elem

Ex: [17,18,5,4,6,1] - > [18,6,6,6,1,-1]

since the last elem does not have anything to the right it would be -1


"""

from typing import List

def replaceElements(arr: List[int]) -> List[int]:
    new_arr = []
    cur_max = float("-inf")
    for n in range(len(arr)-1,0,-1):
        if arr[n] > cur_max:
            cur_max = arr[n]
        new_arr.append(cur_max)
    new_arr = new_arr[::-1]
    new_arr.append(-1)
    return new_arr


Case1 = [17,18,5,4,6,1]

print(replaceElements(Case1))

"""
O(n) time and space complexity as we loop through each elem and put into new array

"""
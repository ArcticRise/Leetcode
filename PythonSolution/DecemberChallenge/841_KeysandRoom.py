"""
There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.

Input: rooms = [[1],[2],[3],[]]
Output: true
Explanation: 
We visit room 0 and pick up key 1.
We then visit room 1 and pick up key 2.
We then visit room 2 and pick up key 3.
We then visit room 3.
Since we were able to visit every room, we return true.


"""

from typing import List
from collections import deque

def canVisitAllRooms(rooms: List[List[int]]) -> bool:
    visited = set()
    queue = deque([0])
    while queue:
        curRoom = queue.pop()
        visited.add(curRoom)
        for i in rooms[curRoom]:
            if i not in visited:
                queue.append(i)
                visited.add(i)
    return len(visited) == len(rooms)

rooms = [[1],[2],[3],[]]
rooms2 = [[1,3],[3,0,1],[2],[0]] #Neg Test Case
print(canVisitAllRooms(rooms))
print(canVisitAllRooms(rooms2))

"""
Time Complexity : O(N + k) _> Vist each room and total num of keys
Space: O(N)

"""
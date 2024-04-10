"""
Given a string find the length of the last word

Ie -> Hello World  = 5 as the length of last word

"""

def lengthOfLastWord(s:str) -> int:
    s.strip()
    arr = s.split()
    return len(arr[-1])

print(lengthOfLastWord("Hello World"))

"""
Time Complexity: O(N)
Space: O(N)

"""
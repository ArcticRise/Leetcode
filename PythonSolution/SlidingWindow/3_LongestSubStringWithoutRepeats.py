"""
Given a string s, find the length of the longest 
substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""

from collections import defaultdict

def lengthOfLongestSubstring( s: str) -> int:
    characters = defaultdict(int)
    left,right,ans = 0,0,0
    while right < len(s):
        if s[right] in characters:
            del characters[s[left]]
            left += 1
        else:
            characters[s[right]] = 1
            #Get max of sliding window
            ans = max((right-left+1),ans)
            right += 1
    return ans


Case1 = "abcabcbb"
print(lengthOfLongestSubstring(Case1))

"""

Time Complexity : O(N)
Space: O(N)

"""
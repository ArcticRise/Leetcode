"""
Given two Strings determine if s is a subsequence of t

ie: abc is a subsequence of abdc but not adcb

"""

def isSubsequence( s: str, t: str) -> bool:
    p1 = p2 = 0
    
    while p1 != len(s) and p2 != len(t):
        if s[p1] == t[p2]:
            p1 += 1
            p2 += 1
        else:
            p2 += 1
    return p1 == len(s)

"""

time complexity O(S+T) which is O(N) b/c we can break it down to the total number of characters
O(1) space complexity

"""

print(isSubsequence("abc","ahhbhhc")) #Case 1 True
print(isSubsequence("abc","ahhchhb")) #Case 2 False
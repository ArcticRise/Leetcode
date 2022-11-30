"""
Given Two Strings Check if both are anagrams of eachother

"""

from collections import Counter

#TypeDef Coding kkkk
def isAnagram(s: str, t: str) -> bool:

    s_count = Counter(s)
    t_count = Counter(t)

    if len(s_count) != len(t_count):
        return False
    for k,v in s_count.items():
        if t_count[k] != v:
            return False
    return True
    

s = "anagram"
t = "nagaram"

print(isAnagram(s,t))

"""
Given two String determine if they are close 

Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

"""
from collections import Counter

def closeStrings(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False
    
    #Count Freq of the words
    freq_count = Counter(word1)
    freq2_count = Counter(word2)
    
    ans = []
    diff = 0
    for k,v in freq_count.items():
        if k not in freq2_count:
            diff += 1
        ans.append(v)
    
    for k,v in freq2_count.items():
        if v not in ans or k not in freq_count:
            diff += 1
        else:
            ans.remove(v)
    return diff == 0


print(closeStrings("abc","bca"))

"""
Time Complexity: 0(N)
Space: O(N) use of map and temp_arr

Top Solution can be written in a more pythonic way

observe below
"""
def closeStrings2(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False
    
    #Count Freq of the words
    freq_count = Counter(word1)
    freq2_count = Counter(word2)
    
    return freq_count.keys()==freq2_count.keys() and sorted(freq2_count.values()) == sorted(freq_count.values())


print(closeStrings2("abc","bca"))

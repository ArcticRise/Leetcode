"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Ex: strs = ["eat","tea","tan","ate","nat","bat"]
output = [["bat"],["nat","tan"],["ate","eat","tea"]]
"""
from typing import List
from collections import defaultdict


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    #Create dictionary with empty list as values
    groups = defaultdict(list)

    #Group Strings
    for s in strs:
        temp = ''.join(sorted(s))
        groups[temp].append(s)
    
    #Append the grouped strings into the list of list for ans
    valid_anagrams = []
    for v in groups.values():
        valid_anagrams.append(v)
    return valid_anagrams


"""
Time Complexity: O(N) ->Loop through every elem in array
Space: O(N) -> use of map and list
"""
Case1 = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(Case1))

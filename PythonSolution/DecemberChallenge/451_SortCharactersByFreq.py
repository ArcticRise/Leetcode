"""
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

s = "tree"
output: "eert"

"""
from collections import defaultdict

def frequencySort(s: str) -> str:
    #First get freq of each String
    freq = defaultdict(int)
    for c in s:
        freq[c] += 1
    
    #Remap freq elems to count
    count_freq = defaultdict(list)
    for k,v in freq.items():
        count_freq[v].append(k)
    
    new_string = ''
    vals = sorted(count_freq,reverse=True)
    for val in vals:
        for c in count_freq[val]:
            new_string += (c*val)
    return new_string


Case1 = "tree"
print(frequencySort(Case1))

"""
Time Complexity: O(NLogN) -> Sorting
Space: O(N)

"""
"""
A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

For example, "Hello World", "HELLO", "hello world hello world" are all sentences.
Words consist of only uppercase and lowercase English letters. Uppercase and lowercase English letters are considered different.

A sentence is circular if:

The last character of a word is equal to the first character of the next word.
The last character of the last word is equal to the first character of the first word.
For example, "leetcode exercises sound delightful", "eetcode", "leetcode eats soul" are all circular sentences. However, "Leetcode is cool", "happy Leetcode", "Leetcode" and "I like Leetcode" are not circular sentences.

Given a string sentence, return true if it is circular. Otherwise, return false.

Input: sentence = "leetcode exercises sound delightful"
Output: true

"""


def isCircularSentence(sentence: str) -> bool:
    if len(sentence) == 1:
        return sentence[0] == sentence[-1]
    
    arr_split = sentence.split()
    last_letter = ''
    for s in arr_split:
        if arr_split[0][0] == arr_split[-1][-1]:
            if last_letter == '':
                last_letter = s[-1]
            elif last_letter == s[0]:
                last_letter = s[-1]
            else:
                return False
        else:
            return False
    return True

Case1 = "leetcode exercises sound delightful"
print(isCircularSentence(Case1))

"""
Time Complexity: O(N)
Space: O(N)

"""
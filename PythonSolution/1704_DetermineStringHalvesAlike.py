"""
Given a string, split the string in half to check if both have same vowel count
 ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

ie _> leetcode -> s1 - leet, s2  - code -> true b/c both vowel count is 2


"""

def halvesAreAlike(s: str) -> bool:
    #Split String in half
    s1,s2 = s[0:len(s)//2], s[len(s)//2:]
    
    #Check for same vowels Count
    c1 = c2 = 0
    for i in s1:
        if i in 'aeiouAEIOU':
            c1 += 1
    
    for j in s2:
        if j in 'aeiouAEIOU':
            c2 += 1

    return c1 == c2

"""
Time Complexity : O(s) -> length of string
Space: O(1)

"""
print(halvesAreAlike("leetcode")) #Pos Testcase
print(halvesAreAlike("ab")) #Neg Testcase


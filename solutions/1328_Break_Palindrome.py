"""
Given a palindromic string of lowercase English letters palindrome, 
replace exactly one character with any lowercase English letter so that the 
resulting string is not a palindrome and that it is the lexicographically smallest one possible.

Return the resulting string. If there is no way to replace a character to make it not a palindrome, 
return an empty string.

A string a is lexicographically smaller than a string b (of the same length) if in the 
first position where a and b differ, a has a character strictly smaller than the 
corresponding character in b. For example, "abcc" is lexicographically smaller than "abcd" 
because the first position they differ is at the fourth character, and 'c' is smaller than 'd'.
"""



class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome)==1:return ""
        for i in range(len(palindrome)):
            if palindrome[i]!='a':
                if i==len(palindrome)//2 and len(palindrome)%2==1:
                    return palindrome[:-1]+'b'                
                palindrome=palindrome[:i]+'a'+palindrome[i+1:]                
                return palindrome
        
        return palindrome[:-1]+'b'
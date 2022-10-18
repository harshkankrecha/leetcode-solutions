"""
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), 
which is then converted into a different digit string.
To determine how you "say" a digit string, 
split it into the minimal number of substrings such that each substring 
contains exactly one unique digit. Then for each substring, say the number of digits, 
then say the digit. Finally, concatenate every said digit.
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        
        def say(s):
            a=[]
            c=1
            for i in range(1,len(s)):
                if s[i]==s[i-1]:
                    c+=1
                else:
                    a.append([s[i-1],c])
                    c=1
            a.append([s[-1],c])
            ans=''
            for x,y in a:
                ans+=str(y)+str(x)
            return ans
            
        
        def helper(n):
            if n==1:
                return "1"
            
            s=helper(n-1)
            return say(s)
        
        return helper(n)
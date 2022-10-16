"""
Given n pairs of parentheses, 
write a function to generate all combinations of well-formed parentheses.
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def isvalid(a):
            stack=[]
            for i in range(len(a)):
                if a[i]=='(':
                    stack.append(a[i])
                else:
                    if len(stack)==0:
                        return False
                    else:
                        stack.pop()
            if len(stack)>0:return False
            return True           
            
        d={'(':n,')':n}  
            
        res=[]
        def helper(ans):
            if len(ans)==n*2:                
                if isvalid(ans):
                    res.append(ans.copy())
                return 
            
            for x in d:
                if d[x]>0:
                    ans.append(x)
                    d[x]-=1
                    helper(ans)
                    d[x]+=1
                    ans.pop()
        helper([])
        fres=[''.join(l) for l in res]
        return fres
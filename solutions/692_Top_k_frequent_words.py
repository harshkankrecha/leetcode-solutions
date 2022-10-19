"""
Given an array of strings words and an integer k, 
return the k most frequent strings.
Return the answer sorted by the frequency from highest to lowest. 
Sort the words with the same frequency by their lexicographical order.
"""

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d={}
        for word in words:
            d[word]=1+d.get(word,0)
        
        a=[(x,d[x]) for x in d]
        ans=sorted(a,key=lambda x:(-x[1],x[0]))[:k]
        return [x[0] for x in ans]
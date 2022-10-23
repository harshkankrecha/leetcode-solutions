"""
You have a set of integers s, which originally contains all the numbers from 1 to n. 
Unfortunately, due to some error, one of the numbers in s got duplicated to another 
number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after 
the error.

Find the number that occurs twice and the number that is missing and return 
them in the form of an array.
TC: O(N)
SC: O(1)
"""



class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        dupli=0
        for i in range(n):
            if nums[i]<0:
                if nums[-nums[i]-1]>0:
                    nums[-nums[i]-1]*=-1
                else:
                    dupli=-nums[i]
            else:
                if nums[nums[i]-1]>0:
                    nums[nums[i]-1]*=-1
                else:
                    dupli=nums[i]
        
        for i in range(n):
            if nums[i]>0:
                return [dupli,i+1]
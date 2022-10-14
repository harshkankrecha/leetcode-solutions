"""
You are given the head of a linked list. Delete the middle node, 
and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from 
the start using 0-based indexing, 
where ⌊x⌋ denotes the largest integer less than or equal to x.

"""



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n=0
        ptr=head
        while ptr!=None:
            ptr=ptr.next
            n+=1
        if n==1:return None
        
        i=0
        p1=None
        p2=head
        while i<n//2:
            p1=p2
            p2=p2.next
            i+=1
        p1.next=p2.next
        return head
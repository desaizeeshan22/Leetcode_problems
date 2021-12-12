class ListNode():
    def __init__(self,value,next=None):
        self.val=value
        self.next=next
a=ListNode(1)
b=ListNode(4)
c=ListNode(5)
a.next=b
b.next=c
d=ListNode(2)
e=ListNode(3)
f=ListNode(7)
d.next=e
e.next=f

def merge_sorted_ll(A,B):
    if A is None:
        return B
    if B is None:
        return A
    if A.val<B.val:
        A.next=merge_sorted_ll(A.next,B)
        return A
    else:
        B.next=merge_sorted_ll(A,B.next)
        return B

m=merge_sorted_ll(a,d)
while m is not None:
    print(m.val)
    m = m.next
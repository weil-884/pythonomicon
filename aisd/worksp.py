#%%<markdown>
# Linked lists
### Complexity O(n)
import numpy
print("suntago less go")
# %%
class Elem:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
        
#%%
head = None
# %%
def printall(head=head):
    curr = head
    while curr != None:
        print(curr.value)
        curr = curr.next

def insertfront(value, head=head):
    new_element = Elem(value, head)
    return new_element

def insertlast(value, head=head):
    if head==None: head = Elem(value,head)
    last=head
    while last.next != None:
        last = last.next
    last.next = Elem(value, None)

def insertlast2(value,head=head,tail=None):
    if head==None:
        head=Elem(value,None)
        tail = head
        return
    tail.next =Elem(value,None)
    tail = tail.next

def insertmiddle(value,index=1):
    pass

def delfirst():
    if head==None: return
    p = head
    head=head.next
    return p

def delmax(head=head):
    prev = head
    curr = head.next
    M = prev.value
    pMax = curr
    
    while curr != None:
        
        if curr.value > M:
            pMax = curr
        
        
        prev=curr
        curr = curr.next
#%%
a = Elem(100)
b = Elem(200, a)
c = Elem(300, b)
head = c

head = insertfront(400, c)
printall(head)

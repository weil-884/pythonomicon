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
    
def insertmiddle(value,index=1):
    pass

#%%
a = Elem(100)
b = Elem(200, a)
c = Elem(300, b)
head = c

head = insertfront(400, c)
printall(head)

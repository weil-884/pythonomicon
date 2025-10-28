#%%
import numpy

# %%
class Node:
    def __init__(self,val,left,right):
        self.val = val
        self.left = left
        self.right = right
        

# %%
def printall_reg(root):
    if root == None:
        return
    print(root.val)
    printall_reg(root.left)
    printall_reg(root.right)

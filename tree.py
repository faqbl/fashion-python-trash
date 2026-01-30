'''
basic tree generation&traversal methods
'''
class Tree:#class definition
    def __init__(self,data):
        self.data=data#initialize as pre_set data or empty
        self.left=None#branch initialize as empty
        self.right=None#same as left branch

def preorder(root):#access order:root node,left branch,right branch
    if not root:
        return#finish traversal
    print(root.data,end=' ')#output before accessing
    preorder(root.left)
    preorder(root.right)
#preorder method is also called dfs

def inorder(root):#access order:left branch,root node,right branch
    if not root:
        return
    inorder(root.left)
    print(root.data,end=' ')#output while accessing
    inorder(root.right)

def postorder(root):#access order:left branch,right branch,root node
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data,end=' ')#output after accessing

def bfs(root):
    if not root:
        return
    queue=["next_line"]#initialize and put in a symbol of newline
    queue.append(root)
    while len(queue)>0:#queue's length>0 means element remaining
        node=queue.pop(0)#pop out the current element for printing
        if isinstance(node,Tree):#make sure the elements in the same line are printed in the same line as well
            print(node.data,end=' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        else:#one line finished,turn to next line,show a newline symbol
            if len(queue)>0:
                queue.append("next_line")
                print()

'''
An example for test(The bfs will obey alphabetical order):
'''

root=Tree('A')
root.left=Tree('B')
root.right=Tree('C')
root.left.left=Tree('D')
root.left.right=Tree('E')
root.right.left=Tree('F')
root.right.right=Tree('G')
preorder(root)
print()
inorder(root)
print()
postorder(root)
bfs(root)

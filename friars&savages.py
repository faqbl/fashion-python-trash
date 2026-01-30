class Tree:
    def __init__(self,a,b,bool):
        self.data=(a,b,bool)
        self.parent=None
        self.children=[]

def form(root):
        a,b,bool=root.data[0],root.data[1],root.data[2]
        if not(a==3 or a==b or a==0):
            root.children=None
        else:
            if bool:
                if a-1>=0:
                    root.children.append(Tree(a-1,b,False))
                if a-2>=0:
                    root.children.append(Tree(a-2,b,False))
                if a-1>=0 and b-1>=0:
                    root.children.append(Tree(a-1,b-1,False))
                if b-1>=0:
                    root.children.append(Tree(a,b-1,False))
                if b-2>=0:
                    root.children.append(Tree(a,b-2,False))
                for i in range(len(root.children)):
                    if root.children[i] is not None:
                        print(root.children[i].data)
                        root.children[i].parent=root
            else:
                if a+1<=3:
                    root.children.append(Tree(a+1,b,True))
                if b+1<=3:
                    root.children.append(Tree(a,b+1,True))
                for i in range(len(root.children)):
                    if root.children[i] is not None:
                        print(root.children[i].data)
                        root.children[i].parent=root
            print()
            for i in root.children:
                form(i)

def dfs(root,target):
    if not root:
        return None
    if root.data==target:
        return root
    for i in root.children:
        dfs(i,target)
    return None

root=Tree(3,3,True)
form(root)
path=[]
temp=dfs(root,(0,0,False))
while temp is not root:
    path.append(temp)
    temp=temp.parent
print(path)

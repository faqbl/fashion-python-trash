import heapq
import copy

def inversion(m):#count the inversion number
    s=[]#set an empty array to flatten the martix
    for i in m:
        for j in i:
            if j!=0:
                s.append(j)
    count=0
    for i in range(8):
        for j in range(i+1,8):
            if s[i]>s[j]:
                count+=1
    return count

def solvable(ini,g):
    """
    in 8-puzzle problem,
    if the inversion number of initial state and the goal state are different in parity,
    the problem can't be solved,
    otherwise there must be a solution
    """
    ini_iv=inversion(ini)
    g_iv=inversion(g)
    return ini_iv%2==g_iv%2

def board_input():
    m=[]
    n=[0,1,2,3,4,5,6,7,8]#for input validity check
    temp=[0]*9#the counter to count the times of occurrence of each legal number
    for i in range(3):
        while True:
            line=list(map(int,input().split()))
            if len(line)!=3:
                print("Error:each line needs 3 numbers,please try again.")
                continue
            if any(num not in n for num in line):
                print("Error:each number should be between 0 and 8,please try again.")
                continue
            m.append(line)
            break
    for i in m:
        for j in i:
            temp[j]+=1
    for i in temp:
        if i!=1:
            print("Error:each number should only appears once,please try again.")
            return board_input()
    return m

class Board:
    def __init__(self,martix,pre=None,move=None,depth=0,goal=None):
        self.board=martix
        self.pre=pre
        self.move=move
        self.g=depth
        self.goal=goal
        self.h=self.one_norm_distance()
        self.f=self.g+self.h

        """
        as we all know,the a star algorithm has a formula
        f=g+h
        to evaluate the path,
        in the formula,suggest there exists a state n,
        f is the cost of the path from star to goal but pass n because of some limits.
        g is the cost of the path from star to n.
        h is the cost of the path from n to goal.
        and in the 8-puzzle problem,
        g comes from DFS algorithm,h is the total Manhattan distances of moving
        """

    def __lt__(self,other):
        return self.f<other.f

    def __eq__(self,other):
        return self.board==other.board

    def __hash__(self):
        return hash(tuple(tuple(row) for row in self.board))
    #turn the board state into tuple in order to hash

    def one_norm_distance(self):#statistics for h(n)
        distance=0
        gp={}
        for i in range(3):
            for j in range(3):
                value=self.goal[i][j]
                gp[value]=(i,j)
        for i in range(3):
            for j in range(3):
                value=self.board[i][j]
                if value!=0:
                    gi,gj=gp[value]
                    distance+=abs(i-gi)+abs(j-gj)
        return distance

    def blank(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return i,j
        return None

    def neighbour(self):
        ns=[]
        i,j=self.blank()
        #find the coordinate of the blank
        moves=\
        [
            ('up',i-1,j),
            ('down',i+ 1,j),
            ('left',i,j-1),
            ('right',i,j+1)
        ]
        for a,ni,nj in moves:
            if 0<=ni<3 and 0<=nj<3:
                nb=copy.deepcopy(self.board)
                nb[i][j],nb[ni][nj]=nb[ni][nj],nb[i][j]
                n=Board(nb,self,a,self.g+1,self.goal)
                ns.append(n)#record all the neighbours in boundary of the blank
        return ns

    def path(self):
        p=[]
        cur=self
        while cur.pre is not None:
            p.append((cur.move,cur.board))
            cur=cur.pre
        #backtrack each moving
        p.reverse()
        #reverse the backtracking is the proper path
        return p

def search(ini,goal):
    start=Board(ini,None,None,0,goal)
    open=[]
    close=set()
    heapq.heappush(open,start)#add start into open list
    while open:
        cur=heapq.heappop(open)
        """
        find the node with the smallest f(n) and treat it as the current node
        p.s. only need to focus on g(n) because the h(n) is certain unless upgrade to a better path or go to the next (best) node
        """
        if cur.board==goal_board:
            sp=cur.path()
            return sp
            #repeat until the goal is in the open list
        close.add(cur)#put it in the close list
        for n in cur.neighbour():#deal with all the neighbours of the current node
            if n in close:
                continue#ignore if it's in close list because it's visited
            in_open=False#suggest that it's not in open list
            for index,op in enumerate(open):#traverse all the
                if n==op:
                    in_open=True#if it has already been in open list,correct the boolean variable
                    if n.f<op.f:#check if it belongs to a better path judge by g(n)
                        open[index]=n
                        heapq.heapify(open)
                        """
                        if g(n) is smaller,means a better path,
                        set the current node as it parent node,
                        re-calculate the g(n) and upgrade the h(n)
                        """
                    break
            if not in_open:
                heapq.heappush(open,n)
                """
                if a neighbour isn't in the open list,
                put it in the open list,
                and set the current node as it parent node
                """
    return None

def print_board(m):
    for i in range(3):
        for j in range(3):
            print(m[i][j],end=" ")
        print()

def action(pre,cur):#find which number of the previous state is located in the blank of the current state
    n=0
    for i in range(3):
        for j in range(3):
            if cur[i][j]==0:
                n=pre[i][j]
    return n

print("Please input 0~8 for only once to form a 3×3 board with a blank represented by 0 as questioning a 8-puzzle problem.")
print("This program will solve your problem unless it is not solvable.")
print("Please input initial board in a 3×3 matrix:")
ini_board=board_input()
print("This is the initial board:")
print_board(ini_board)
print("Please input initial board in a 3×3 matrix:")
while True:
    goal_board=board_input()
    if ini_board==goal_board:
        print("Please don't set the goal board as same as the initial board,try again.")
        continue
    else:
        break
print("This is your goal board:")
print_board(goal_board)
ini_iv=inversion(ini_board)
goal_iv=inversion(goal_board)
bool_flag=solvable(ini_board,goal_board)
if not bool_flag:
    print("No solution!")
    print("Reason:the inversion numbers of the initial board and the goal board are different in parity.")
    exit(1)
s=search(ini_board,goal_board)
p=len(s)
print("Solution found!")
print(f"It takes {p} steps:")
print("Step 0:initial board:")
print_board(ini_board)
pre_board=ini_board
r={'up':'↓','down':'↑','left':'→','right':'←'}
"""
what we have recorded is the moving of the blank,
so we need a dictionary loading the op-direction for display
"""
for step,(move,board) in enumerate(s,1):
    print(f"Step {step}:{action(pre_board,board)}{r.get(move)}.")
    print_board(board)
    pre_board=board
print("Accomplished.")

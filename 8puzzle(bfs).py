import copy
from collections import deque

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

class Board:
    def __init__(self,matrix,pre=None,move=None,depth=0):
        self.board=matrix
        self.pre=pre
        self.move=move
        self.depth=depth

    """
    just need depth as a variable to count the step
    """

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(tuple(tuple(row) for row in self.board))
    # turn the board state into tuple in order to hash

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
                n=Board(nb,self,a,self.depth+1)
                ns.append(n)#record all the neighbours in boundary of the blank
        return ns

def bfs(ini,goal):
    start=Board(ini)
    end=Board(goal)
    queue=deque([start])
    visited={start:None}
    r_queue=deque([end])
    r_visited={end:None}
    meet=None#record the meeting point of two ways
    while queue and r_queue:
        cur_len=len(queue)#forward(start from initial state)
        for i in range(cur_len):
            cur=queue.popleft()
            if cur in r_visited:
                meet=cur
                break
            for n in cur.neighbour():
                if n not in visited:
                    visited[n]=cur
                    queue.append(n)
        if meet:
            break
        curr_len=len(r_queue)#backward(start from goal state)
        for i in range(curr_len):
            curr=r_queue.popleft()
            if curr in visited:
                meet=curr
                break
            for n in curr.neighbour():
                if n not in r_visited:
                    r_visited[n]=curr
                    r_queue.append(n)
        if meet:
            break
    path=[]
    r_path=[]
    cur=meet
    """
    backtrack from the meeting point to the start points(forward and backward)
    to record the path and combine
    """
    while cur!=start:
        path.append((cur.move,cur.board))
        cur=visited[cur]
    path.reverse()#need to reverse because backtracking
    cur=meet
    while cur!=end:
        pre=r_visited[cur]
        r_move=reverse(cur.move) if cur.move else None
        r_path.append((r_move,pre.board))
        cur=pre
        #no need to reverse because two negatives make a positive
    path+=[(None,meet.board)]+r_path
    return path

def reverse(move):
    r={'up':'down','down':'up','left':'right','right':'left'}
    return r.get(move)
    #unifiedly show as the moving of blank in proper direction

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

def print_board(m):
    for i in range(3):
        for j in range(3):
            print(m[i][j],end=' ')
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
p=bfs(ini_board,goal_board)
print("Solution found!")
print(f"It takes {len(p)-1} steps:")
print("Step 0:initial board:")
print_board(ini_board)
pre_board=ini_board
step=0
symbol={'up':'↓','down':'↑','left':'→','right':'←'}
for move,board in p:#the path record the meeting point twice repeatedly,and we just need to display once
    if move is not None:
        step+=1
        print(f"Step {step}:{action(pre_board,board)}{symbol.get(move)}.")
    print_board(board)
    pre_board=board
print("Accomplished.")

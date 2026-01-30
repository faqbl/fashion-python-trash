'''
basic graph generation&traversal algorithm
'''
from collections import defaultdict
from collections import deque

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)

    def addEdge(self,u,v,weight=None):
        self.graph[u].append((v,weight))#define vertex,edge,weight as key-value pairs
        #self.graph[v].append((u,weight))only undirected graphs need

    def dfs(self,start):
        visited=set()#define an empty set to store the visited node,initialized as empty because no element is visited at first
        stack=[start]#define a stack to traverse through the graph
        while stack:
            vertex=stack.pop()
            if vertex not in visited:
                print(vertex,end=' ')
                visited.add(vertex)
                for n in reversed(self.graph[vertex]):#traverse in reverse order to make sure the traverse order is always consistent
                    if n[0] not in visited:
                        stack.append(n[0])#push the not visited neighbour into the stack to traverse

    def bfs(self,start):
        visited=set()
        queue=deque([start])
        while queue:
            vertex=queue.popleft()
            if vertex not in visited:
                print(vertex,end=' ')
                visited.add(vertex)
                for n in self.graph[vertex]:#traverse in proper order to make sure each not-visited neighbour is visited first
                    if n[0] not in visited:
                        queue.append(n[0])

'''
An example for test(The bfs will obey alphabetical order):
'''

test=Graph()
test.addEdge('A', 'B')
test.addEdge('A', 'C')
test.addEdge('B', 'D')
test.addEdge('C', 'E')
test.addEdge('D', 'E')
test.dfs('A')
print()
test.bfs('A')

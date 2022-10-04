
from collections import defaultdict
class Graph:
	
	def __init__(self):

		# default dictionary to store graph
		self.graph = defaultdict(list)

	def addEdge(self,u,v):
		self.graph[u].append(v)

	def BFS(self, s):

	
		visited = [False] * (len(self.graph))

		queue = []

		
		queue.append(s)
		visited[s] = True

		while queue:

			
			s = queue.pop(0)
			print (s, end = " ")

			for i in self.graph[s]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print ("Following is Breadth First Traversal"
				" (starting from vertex 2)")
g.BFS(2)


output :-
	
Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

========================== RESTART: V:\BFS problem.py ==========================
Following is Breadth First Traversal (starting from vertex 2)
2 0 3 1 


class checkConnectivity(object):
	def __init__(self,userlist,graph,mapping):
		self.userlist=userlist
		self.graph=graph
		self.mapping=mapping

	def userExists(self,l,m):
		for i in l:
			if i not in m:
				return 0
		return 1

	def bfs(self,g,seed,userlist):
		queue=[]
		queue.append(seed)
		visited=[]
		while(queue):
			popped=queue.pop(0)
			visited.append(popped)
			for i in g[popped]:
				if i not in visited and i not in queue:
					queue.append(i)
		return visited

	def check(self):
		if self.userExists(self.userlist,self.mapping):
			ulist=[]
			ulist=[self.mapping[i] for i in self.userlist]
			seed=ulist[0]
			l1=self.bfs(self.graph,seed,ulist)
			l1=set(l1)
			l2=set(ulist)
			if l2.issubset(l1):
				return 1
			else:
				return 0
		else:
			return -1

class getDegree(object):
	def __init__(self,user1,user2,graph,mapping):
		self.user1=user1
		self.user2=user2
		self.graph=graph
		self.mapping=mapping

	def userExists(self,u1,u2,m):
		if u1 in m and u2 in m:
			return 1
		else:
			return 0

	def bfs(self,g,start,end):
			current=[start]
			count=0
			visited_prev=[]
			visited=[]
			while end not in current:
				visited.extend(current)
				visted=list(set(visited)-set(visited_prev))
				for i in visited:
					current.extend(g[i])
				count=count+1
				visited_prev=visited
			return count

	def get(self):
		if self.userExists(self.user1,self.user2,self.mapping):
			start=self.mapping[self.user1]
			end=self.mapping[self.user2]

			t=[self.user1,self.user2]
			temp=checkConnectivity(t,self.graph,self.mapping)
			if temp.check():
				return self.bfs(self.graph,start,end)
			else:
				return 0
		else:
			return -1
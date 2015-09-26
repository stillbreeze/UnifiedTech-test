class createGraph(object):
	def __init__(self):
		pass

	def createGraph(self):
		graph={}
		return graph

	def createMapping(self):
		mapping={}
		return mapping

class createUser(object):
	def __init__(self,username,graph,mapping):
		self.firstname=username.split(' ')[0]
		if ' ' in username:
			self.lastname=username.split(' ')[1]
		else:
			self.lastname=''
		self.graph=graph
		self.mapping=mapping

	def checkExisting(self,f,l,m):
		if (f + ' ' + l) in m:
			return 1
		else:
			return 0

	def makeNode(self):
		if not self.checkExisting(self.firstname,self.lastname,self.mapping):
			current=len(self.graph)+1
			self.graph[current]=[]
			if self.lastname:
				self.mapping[self.firstname + ' ' + self.lastname]=current
			else:
				self.mapping[self.firstname + '' + self.lastname]=current
			return 1
		else:
			return 0

class createFriends():
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

	def makeLinks(self):
		if( self.user1!=self.user2 and self.userExists(self.user1,self.user2,self.mapping) ):
			val1=self.mapping[self.user1]
			val2=self.mapping[self.user2]
			self.graph[val1].append(val2)
			self.graph[val2].append(val1)
			return 1
		else:
			return 0
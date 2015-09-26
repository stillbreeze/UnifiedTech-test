from createGraph import createGraph,createUser, createFriends
from queryGraph import checkConnectivity, getDegree
a = createGraph()
g = a.createGraph()
m = a.createMapping()
count = 0


while 1:
	if count==0 or count==1:
		choice = raw_input("\n\nChoose:\n0. Exit\n1. Add a user\n")
	elif count>=2:
		choice = raw_input("\n\nChoose:\n0. Exit\n1. Add a user\n2. Add a friend link\n3. Check connectivity\n4. Check degree of connection\n")

	count = count+1

	if choice=='0':
		break
	elif choice=='1':
		username=raw_input("Enter a username:\t")
		b = createUser(username,g,m)
		if b.makeNode():
			print "User created"
		else:
			print "User already exists"
	elif choice=='2':
		user1,user2 = raw_input("Enter the usernames of each user seperated by a tab:\t").split('\t')
		c = createFriends(user1,user2,g,m)
		if c.makeLinks():
			print "Friendship link established"
		else:
			print "Either user doesn't exist or both names given are the same"
	elif choice=='3':
		print "Enter names seperated by Enter key. Press 0 to stop\n\n"
		l=[]
		while 1:
			temp=raw_input("Enter name:\t")
			if temp=='0':
				break
			l.append(temp)
		d = checkConnectivity(l,g,m)
		temp = d.check()
		if temp==-1:
			print "User doesn't exist"
		elif temp==0:
			print "Given network of users are not connected"
		else:
			print "Given network of users are connected"
	elif choice=='4':
		user1,user2 = raw_input("Enter the usernames of each user seperated by a tab:\t").split('\t')
		e = getDegree(user1,user2,g,m)
		temp = e.get()
		if temp==-1:
			print "User doesn't exist"
		elif temp==0:
			print "Given network of users are not connected"
		else:
			print "%s and %s are %d degree connections" %(user1,user2,temp)


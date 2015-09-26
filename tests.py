from createGraph import createGraph,createUser, createFriends
from queryGraph import checkConnectivity, getDegree

print "\n\nCreating the schema:\n"

a = createGraph()
g = a.createGraph()
m = a.createMapping()


print "\n\nTesting user creation:\n"


b = createUser("Immanuel Kant",g,m)
if b.makeNode():
	print "Node added successfully"
else:
	print "TEST CASE FAILED"

b = createUser("Elon Musk",g,m)
if b.makeNode():
	print "Node added successfully"
else:
	print "TEST CASE FAILED"

b = createUser("Voltaire",g,m)
if b.makeNode():
	print "Node added successfully"
else:
	print "TEST CASE FAILED"

b = createUser("Mark Twain",g,m)
if b.makeNode():
	print "Node added successfully"
else:
	print "TEST CASE FAILED"

b = createUser("Abraham Lincoln",g,m)
if b.makeNode():
	print "Node added successfully"
else:
	print "TEST CASE FAILED"

b = createUser("Bertrand Russel",g,m)
if b.makeNode():
	print "Node added successfully"
else:
	print "TEST CASE FAILED"

b = createUser("Stephen Hawking",g,m)
if b.makeNode():
	print "Node added successfully"
else:
	print "TEST CASE FAILED"

b = createUser("Steve Jobs",g,m)
if b.makeNode():
	print "Node added successfully"
else:
	print "TEST CASE FAILED"


print "\n\nTesting friendship creation:\n"


c = createFriends("Immanuel Kant","Elon Musk",g,m)
if c.makeLinks():
	print "Link added successfully"
else:
	print "TEST CASE FAILED"

c = createFriends("Immanuel Kant","Mark Twain",g,m)
if c.makeLinks():
	print "Link added successfully"
else:
	print "TEST CASE FAILED"

c = createFriends("Immanuel Kant","Steve Jobs",g,m)
if c.makeLinks():
	print "Link added successfully"
else:
	print "TEST CASE FAILED"

c = createFriends("Voltaire","Elon Musk",g,m)
if c.makeLinks():
	print "Link added successfully"
else:
	print "TEST CASE FAILED"

c = createFriends("Bertrand Russel","Elon Musk",g,m)
if c.makeLinks():
	print "Link added successfully"
else:
	print "TEST CASE FAILED"

c = createFriends("Abraham Lincoln","Stephen Hawking",g,m)
if c.makeLinks():
	print "Link added successfully"
else:
	print "TEST CASE FAILED"


print "\n\nTesting connectivity:\n"



userlist=["Immanuel Kant","Bertrand Russel"]
d = checkConnectivity(userlist,g,m)
if d.check():
	print "TEST CASE PASSED"
else:
	print "TEST CASE FAILED"

userlist=["Elon Musk","Voltaire","Abraham Lincoln"]
d = checkConnectivity(userlist,g,m)
if not d.check():
	print "TEST CASE PASSED"
else:
	print "TEST CASE FAILED"

userlist=["Immanuel Kant","Bertrand Russel","Stephen Hawking","Steve Jobs"]
d = checkConnectivity(userlist,g,m)
if not d.check():
	print "TEST CASE PASSED"
else:
	print "TEST CASE FAILED"

userlist=["Stephen Hawking","Abraham Lincoln"]
d = checkConnectivity(userlist,g,m)
if d.check():
	print "TEST CASE PASSED"
else:
	print "TEST CASE FAILED"

userlist=["Stepen Hing","Abraham Lincoln"]
d = checkConnectivity(userlist,g,m)
if d.check()==-1:
	print "TEST CASE PASSED"
else:
	print "TEST CASE FAILED"

userlist=["Abraham Lincoln","Donald Bren"]
d = checkConnectivity(userlist,g,m)
if d.check()==-1:
	print "TEST CASE PASSED"
else:
	print "TEST CASE FAILED"



print "\n\nTesting degree calculation:\n"



user1 = "Bertrand Russel"
user2 = "Steve Jobs"
e = getDegree(user1,user2,g,m)
if e.get()==3:
	print "TEST CASE PASSED"
else:
	print "TEST CASE FAILED"

user1 = "Bertrand Russel"
user2 = "Voltaire"
e = getDegree(user1,user2,g,m)
if e.get()==2:
	print "TEST CASE PASSED"
else:
	print "TEST CASE FAILED"

user1 = "Voltaire"
user2 = "Mark Twain"
e = getDegree(user1,user2,g,m)
if e.get()==3:
	print "TEST CASE PASSED"
else:
	print "TEST CASE FAILED"

user1 = "Elon Musk"
user2 = "Abraham Lincoln"
e = getDegree(user1,user2,g,m)
if e.get()==0:
	print "TEST CASE PASSED"
else:
	print "TEST CASE FAILED"

user1 = "Elon Mus"
user2 = "Abraham Lincoln"
e = getDegree(user1,user2,g,m)
if e.get()==-1:
	print "TEST CASE PASSED"
else:
	print "TEST CASE FAILED"
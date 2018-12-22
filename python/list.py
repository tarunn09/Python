#!/usr/bin/python
users = ["user1", "user2", "user3"]
print  (users[0])
print (users[len(users)-1])
print (users[-1])
print (users[-2])
users.append("peter")
print (users)
print (users[-1] + " " + users[-2])
#insert add an item at speific index
users.insert(1,"mary")
users.remove("user1")
print (users)
print (sorted(users))
print (users)
for u in users:
    print ("Username is ",u.titleprint ())
	

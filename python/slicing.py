#!/usr/bin/python
users = ["user1", "user2", "user3", "users4"]
print (users[1:3])
print (users[1:]) #starting from second to last
print (users[1:-1])
print (users[:-3])  #print from fisrt 3rd items
print (users[::-1]) #print reverse list
print (users[1:-1]) 
print (users[1:-1:-1])

num = "123"
users= [u+num for u in users]
print (users)
lst  =  [x ** 2  for x in range (1, 11)   if  x % 2 == 1]
print (lst)
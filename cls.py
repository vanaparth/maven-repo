#!usr/bin/python
class Person:
   def __init__(self):
    print("our class is created")
   def setFullName(self,firstname,lastname):
	self.firstname=firstname
	self.lastname=lastname
   def prinFullname(self):
    print(self.firstname," ",self.lastname)
personName=Person()
personName.setFullName('programming','knowledge'
)
personName.prinFullname()
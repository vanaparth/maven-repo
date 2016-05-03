class Parent:
	value1="this is value 1"
	value2="this is value 2"
class Sibling (Parent):
     pass
class Child (Parent):
     pass
 
parent=Parent()
print(parent.value1)
print(parent.value2)

sibling= Sibling()
print(sibling.value1)
print(sibling.value2)

child=Child()
print(child.value1)
print(child.value2)
 

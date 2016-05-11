import random
heighest=10
answer=random.randrange(heighest)
guess=raw_input("enter the number from 0 to %d"%heighest)

while (int(guess)!= answer):
   if(int(guess)<answer):
     print ("the number is heigher")
   else:
     print ("the number is lower")
     guess = raw_input("enter the number from 0 to %d",heighest)
raw_input("you are at winner face")
r
highest = 10
answer = 7
guess = raw_input("guess a number from 0 to %d:"%highest)
while(int(guess)!=answer):
   if(int(guess)<answer):
      print "answer is heigher"
   else:
      print "answer is lower"
   guess = raw_input("guess number from 0 to %d"%highest)
raw_input("you are a winner face")
"""
try :

   x = 5+'ham'
   print "x"
   
except:
     print "exception in code"
	 
"""

#raise TypeError("hahhaha")

try:
  x = 5 + "ham"
  print x
except ZeroDivisionError:
    print "will not see this"

finally:
    print "the final word"
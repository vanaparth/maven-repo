class Person:
      def FirstName(self,firstName,lastname):
	   self.firstName=firstName
	   self.lastname=lastname
      def Fullname(self):
	   print(self.firstName," ",self.lastname)
personnew=Person()
personnew.FirstName("raj","van")
personnew.Fullname()		   
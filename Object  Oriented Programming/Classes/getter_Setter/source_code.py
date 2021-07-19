class abc():
	Name="None"
	__Roll=0
	def __init__(self):
	    pass
	def setname(self,n):
		self.Name=n
	def setroll(self,r):
		self.Roll=r

	def getname(self):
	    return self.Name
	def getroll(self):
		return self.Roll
	def display(self):
		print("Name is "+ str(self.getname()))
		print("Roll is " +str(self.getroll()))


obj= abc()
n= input("Enter the Name : ")
obj.setname(n)

r= int(input("Enter the Roll No :"))
obj.setroll(r)

obj.display()

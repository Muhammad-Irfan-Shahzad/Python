class abc():
	Name="None"
	__Roll=0
	def __init__(self,n,r):
		self.Name=n
		self.Roll=r

	def getname(self):
	    return self.Name
	def getroll(self):
		return self.Roll
	def display(self):
		print("Name is "+ str(self.getname()))
		print("Roll is " +str(self.getroll()))


n= input("Enter the Name : ")
r= int(input("Enter the Roll No :"))

obj= abc(n,r)

obj.display()

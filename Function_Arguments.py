print("function argument")
#position argument

def Batch1(name ,fees):
	print("batch name is",name)
	print("fees are",fees)

#print("==Demonstration of Position Argumets==")
#Batch1('python',5000)
#Batch1(5000,'Angular')

print("=============")
#eyword argument

def batch2(name, fees):
	print("batch name is ",name)
	print("fees are",fees)

print("====Keyword of Argument===")

#batch2(fees=9000,name='PPA')
#batch2(name='LB',fees=75000)
print("==============")

def batch3(name,fees=5000):
	print("batch name is",name)
	print("fees are",fees)
print("===Default Argument===")

#batch3('angular',7500)
#batch3('lb')
#batch3('PPa',fees=9000)
#batch3(name='lb')

print("=============")
def Add(*no):
	ans=0
	for i in no:
		ans=ans+1
	return ans
print("==variable number of argument")
#ret=Add(10,20,30)
#print(" is",ret)

#ret=Add(10,20,30,40,50,60)
#print("argument is",ret)

#ret =Add(10,20)
#print("Argument is",ret)

def StudentInfo(**other):
	print(other)
	for i,j in other.items():
		print(i,j)

print("==Keyword variable number===")
StudentInfo(age=21,address="PICT",mobile=8792922866,company='marvellous')








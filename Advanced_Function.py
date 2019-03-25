print("example of Advance Function")

print("=========1================")
#Function which accept value and return nothing
no=11
def Display1():
	print("Display1")
#Display1()
#function which accepts value and return nothing

print("=======2==========")
def Display2(value):
	print("Inside Display2")
	print("Accepted value is",value)

#Display2(no)


#Function which accepts value and return value
print("======3===========")
def Display3(value):
	print("Inside Display3")
	print("Accepted value is ",value)
	return value+1

#ret=Display3(no)
#print("return value is",ret)

print("========4=============")

def Display4(value1,value2):
	print("Inside Dispaly4")
	Add= value1+value2
	sub=value1-value2
	return Add , sub 

ret1,ret2=Display4(10,4)
print("Addition is ",ret1)
print("Substraction is",ret2)
#Display4(Add,sub)

print("=======5========")
def Display5():
	print("Inside Dispaly5")
	Display1()

#Display5()

print("==========6==========")
# Function which contains another 
#nested function defined in it.

def Display6():
	print("inside Display6")
	def InnerFun():
		print("Inside InnerFunction")
	InnerFun()

#Display6()
print("========end=========")





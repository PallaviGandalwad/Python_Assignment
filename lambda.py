print("lambda")

#define regular function

def add(no1,no2):
	return no1+no2

value1=10
value2=5

#ret =add(value1,value2)
#print("Addition is {} with regular function".format(ret))

fp =lambda no1,no2:no1+no2
ret=fp(value1,value2)
print("Addition is {} lambda function".format(ret))
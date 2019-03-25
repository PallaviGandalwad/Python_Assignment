print("Dynamic in list")
arr=list()#object of list

num=input("Enter how many element you want->>")
print("Enter number in array:")
# Iterate the for loop to accept N numbers

for i in range(0,int(num)):
	#enter individual number from user
	no=input("num:")

	#insert that element into list
	arr.append(int(no))

print("Entered elements are : ",arr)
 


# As there is no direct support for array 
#in python we have to import array module to
#create array
import array as arr

a=arr.array('i',[2,4,6,8])## is is considered as type code
print("\n")
print("First element:",a[0])#2
print("Second element:",a[1])#4
print("second last element:", a[-1])#8
print("\n")
print(a.typecode)#i
print("=========================================================")
a = arr.array('f', [2.4, 4.5, 6.5, 8.8]) # is is considered as type code
print("\n")
print("First element:",a[0])
print("Second element:",a[1])
print("second last element:", a[-1])
print("\n")
print(a.typecode)#f
print("===================================")

a.reverse()
for i in range(len(a)):
	print(a[i])

print("===========================")
b=arr.array('i',[1,2,1,2])
for i in range(len(b)):
	print(b[i])
#output:1 2 1 2
print("============================")
i=0
while (i<len(b)):
	print(b[i])
	i+=1












print("python")
print("example of string")

name="marvellous"

newName='marvel'

print(name)

print(type(name))

print("============")
print(newName)
print(type(newName))


# as String is array of characters 
#we can access using subscript operator

print("=====")
print(name[0])
print(name[1])
print(name[9])

#print(name[10]) #Index out of bound
#negative index access elements from right to left
print("==")
print(name[-1])
print(name[-2])
print(name[-3])
print("===========")
# We can also print characters in range
print(name[0:3])#mar
print(name[2:3])#r
print(name[2:])#1st and 2nd letter is skip 'rvellous'
print(name[:3])#prints aonly 'mar'

print("=================")
# strings in python are immutable
#name[0]='m'
print("=============")
#we can use len function to calculate length of string
print(len(name))
print(len(newName))

#strip method removes whitespaces 
#from begining and end
className="  Marvellous        Infosystem Pune    "
print(className.strip())
print("++++++++++++")
# By using split we can tokanize the strinng
Batchs = "PPA,LB,Angular,Python,C#,Project,UNNIX,LSP"
print(Batchs.split(","))
print("========")
Batchs = "PPA,LB,Angular,Python,C#,Project,UNNIX,LSP"
print(Batchs.split(" "))#no effect
print("====")
Batchs = "PPA,LB,Angular,Python,C#,Project,UNNIX,LSP"
print(Batchs.split("-"))#no effect
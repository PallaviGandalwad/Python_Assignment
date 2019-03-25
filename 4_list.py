print("python russum")
print("List example")

batch=["PPA","LB","Angular","python"]

print(batch)

print(batch[0])
print(batch[3])
print(batch[-1])
print(batch[1:]) #//1 lasodun bakii srv print krne
print(batch[:3])#3 la sodun baki srv print krnee

#heterogenious data

data1=[11,"marvellous",3.14]
print(data1)

data2=[21,"infosystem",6.10]
print(data2)

#we create list of list
print("========================")
combined=[data1 , data2]
print(combined)


#There are multiple methods 
#that we can use to manipulate list
print("=============")
batch.append("mean")
print(batch)

print("==============")
batch.insert(2,"LSP")#at arr position 2nd la LSP lihun ale
print(batch)

print("=================")
batch.remove("LSP")
print(batch)

print("===")
batch.pop()
print(batch)

batch.pop()#element are deleted  from left to right
print(batch)

print("=========")
del batch[3:]#it prints the 1 2 3 elements
print(batch)
print("=========")
del batch[2:]#it prints only 2nd elements
print(batch)
print("=========")
del batch[1:]#it prints the 1st elements
print(batch)
print("=============================")
print(batch)
print("==========")
batch.extend(["LB","Python","Angular","C","pPA"])
print(batch)#it prnts all extended batch with old one is attached at first ppa,lb and all other

batch.sort()#it prints by the using 1st letter as capital letter
print(batch)
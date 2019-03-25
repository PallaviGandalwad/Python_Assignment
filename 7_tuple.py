print("---- Marvellous Infosystems by Piyush Khairnar-----")
print("Demonstration of Tuples")
tup = (11,"Marvellous",3.14,51,"Infosystems")#as it is from (touple)
print(tup)
print("========")
print(tup[0])#11
print("========")
print(tup[1])#Marvellous
print("======")
print(tup[1:])#1st element is not present
#output:->'Marvellous',3.14,51,'Infosystems'
print("=====")
print(tup)#
print(tup[:2])# 11,"Marvellous
print(tup[:3])#11,"Marvellous",3.14
print(tup[:4])
print("====")
print(tup[1:3])#skip 1st print 2nd & 3rd element
print(tup[1:2])#only 2nd element
# tup[1] = "marvellous" It is not allowed to change the contents
print(len(tup))
print("==")
print("M" in tup)#Mis not present in tuple
print("===")
print("Marvellous" in tup)
#print("=====")
del tup#only blanck space 
 
print("python")
print("exampleof set")

demo={11,"PPA",21,3.14,"Python"}
print(demo)

print("==========")
print(len(demo))
print("==========")
demo.remove(3.14)
print(demo)

print("==========")

demo.discard(11)#there is not 11 in the set
print(demo)

print("==========")

demo.add("Angular")
print(demo)
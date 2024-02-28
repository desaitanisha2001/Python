d={1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h"}
print(d)
print(d[3])
print(d.get(3))
print(d.items())
print(d.keys())
print(d.values())
print(d.pop(3))
print(d)
d1={9:"i",10:"j"}
d.update(d1)
print(d)
d.popitem()
print(d)
for i in d:
    print(i," : ",d[i])

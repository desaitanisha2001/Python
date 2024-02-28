s=input("Enter N:")

char=0
num=0
sp=0
upcase=0
lowcase=0

for i in s:
    if i.isalpha():
        char=char+1   
    elif i.isspace():
        sp=sp+1   
    elif i.isnumeric(): 
        num=num+1
    if i.isupper():
        upcase=upcase+1
    elif i.islower():
        lowcase=lowcase+1


print("Enter number of alphabets:",char)
print("Enter number of numeric:",num)
print("Enter number of space:",sp)
print("Enter number of upper case:",upcase)
print("Enter number of lower case:",lowcase)

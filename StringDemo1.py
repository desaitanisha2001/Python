s=input("Enter a string:")
al=0
num=0
sp=0
upper=0
lower=0

for i in s:
    if i.isalpha():
        al=al+1
    elif i.isspace():
        sp=sp+1
    elif i.isnumeric():
        num=num+1
    if i.isupper():
        upper=upper+1
    elif i.islower():
        lower=lower+1
print("Total number of alphabets:",al)
print("Total number of numericals:",num)
print("Total number of space:",sp)
print("Total number of upper case:",upper)
print("Total number of lower case:",lower)

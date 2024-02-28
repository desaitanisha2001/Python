n=int(input("Enter n:"))
if n%2!=0:
    for i in range(3,int(n/2)+1,2):
        if n%i==0:
           print(n,"is not prime")
           break

n=int(input("Enter N:")
a,b=0,1
print(a,end=" ")
while b<n:
    print(b,end=" ")
    a,b=b,a+b

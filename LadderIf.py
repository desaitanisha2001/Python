rno=int(input("Enter Roll No:"))
sname=(input("Enter Student Name:"))
s1=int(input("Enter Marks of subject 1:"))
s2=int(input("ENter Marks of subject 2:"))
s3=int(input("Enter Marks of subject 3:"))

total =s1+s2+s3
per=total/3
if per>=70:
    print("distinction")
elif per>=60:
    print("The result is A grade")
elif per>=50:
    print("The result is B grade")
elif per>=40:
    print("The result is C grade")
else:
    print("Fail")

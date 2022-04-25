a=int(input("enter the first no:-"))
b=int(input("enter the second no:-"))
c=int(input("enter the third no:-"))
d=int(input("enter the fourth no:-"))
if a>b and  a>c and a>d:
	print("greatest no si:-",a)
elif b>c and b>d:
	print("greatest no is:-",b)
elif c>d:
	print("greatest no is:-",c)
else:
	print("greatest no is:-",d)
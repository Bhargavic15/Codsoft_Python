x=int(input("Enter First value"))
y=int(input("Enter Second value"))

z=int(input("Enter operation you want to perform: 1.Add, 2.Sub, 3.Mul, 4.Div"))

if z==1:
    print(x+y)

elif z==2:
    print(x-y)

elif z==3:
    print(x*y)

elif z==4:
    print(x/y)

else:
    print("Invalid")

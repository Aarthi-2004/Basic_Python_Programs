A=int(input("value of 1:"))
B=int(input("Value of 2:"))
choose = input("The operation to perform(+,-,*,//): ")

if(choose=='+'):
    print(A+B)
elif(choose=='-'):
    print(A-B)
elif(choose=='*'):
    print(A*B)
else:
    print(A//B)

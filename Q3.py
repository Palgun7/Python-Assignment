a= int(input("Enter number:"))
fact=1
if(a<0):
    print("Factorial doesnt exist")
elif(a==0):
    print("Factorial of 0 is 1")
else:
    for i in range(1,a+1):
        fact *= i
    print("Factorial of ",a,"is",fact)


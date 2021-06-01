def multFunc(m,n):
    a=range(n,(n*m)+1,n)
    print(*a)
x= int(input("Enter the number:"))
y=int(input("Enter the number of multiples:"))
multFunc(y,x)

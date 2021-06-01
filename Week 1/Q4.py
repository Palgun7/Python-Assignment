numterms = int(input("Enter number of terms: "))
a1=0
a2=1
count=0
print("Fibonacci series:")
while count<numterms:
    print(a1)
    nth = a1+a2
    a1=a2
    a2=nth
    count = count+1
print("End")

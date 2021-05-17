givenArray = ["1","-6","3","-1","10"]
l=len(givenArray)
pos = 0
neg = 0
for i in range(0,l):
    if(int(givenArray[i]) > 0):
        pos += int(givenArray[i])
    else:
        neg += int(givenArray[i])

if(pos>abs(neg)):
    print("POSITIVE")
else:
    print("NEGATIVE")
print(pos,neg)
filename="cars"
file=open(filename,"r")
length=0
count=0
for l in file:
    words=l.split()
    for a in words:
        x=len(a)
        count=count+x
    le=len(words)
    length=length+le
    print("\n")
print("number of words",length)
print("coiunt of letters",count)
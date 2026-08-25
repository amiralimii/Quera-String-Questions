a=int(input( ))
os=[]
ts=[]
for i in range(a):
    ms=input( )
    lines=ms.split("\n")
    for line in lines:
        names=line.split(" ")
        os.append(names[0])
for o in os:
    k=os.count(o)
    ts.append(k)
print(max(ts))

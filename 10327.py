an,target=input( ).split(" ")
sort=sorted(set(target))
found=False
FINSH=[]
for i in range(int(an)):
    if sorted(set(input( ).strip( )))==sort:
        FINSH.append("Yes")
    else:
        FINSH.append("No")
for F in FINSH:
    print(F)

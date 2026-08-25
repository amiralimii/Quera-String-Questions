counts=[]
lines=[]
for i in range(5):
    ms=input( )
    counts.append(ms)
for i in range(5):
    if "MOLANA" in counts[i] or "HAFES" in counts[i]:
        lines.append(i+1)
if lines:
    print(*lines)
else:
    print("NOT FOUND!")

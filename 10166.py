n=int(input( ))
answers=input( )
scores1=0
scores2=0
scores3=0
p1=[3,3,1,1,2,2]
p2=[1,2,3]
p3=[2,1,2,3] 
for i in range(n):
    carrect=int(answers[i])
    if carrect==p1[i%len(p1)]:
        scores1+=1
    if carrect==p2[i%len(p2)]:
        scores2+=1
    if carrect==p3[i%len(p3)]:
        scores3+=1
b={"keyvoon":scores1,"nezam":scores2,"shir farhad":scores3}
k=max(b.values( ))
print(k)
ts=dict(sorted(b.items( ),key=lambda a:a[1],reverse=True)) 
for name,score in ts.items( ):
    if score==k:
        print(name) 

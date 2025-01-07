#Szabó Bálint, Varga Zoltán 10.b, Python első beadandó
#a feladat
t=[10, 0, 18, 15, 22, 10, 14, 28, 4, 6, 0, 9]
n=len(t)
print(t)
poz=0
neg=0

for i in range(0,n-1):
    for j in range(i+1,n):
        if(t[i]<t[j]):
            poz+=1
        if(t[i]>t[j]):
            neg+=1
if(poz>neg):
    print("Igaz, hogy mindig több szállt fel, mint le!")
if(poz<neg):
    print("Nem igaz, hogy mindig több szállt fel, mint le!")

#b feladat
tb=[2, 0, 4, 1, 15, 11, 100, 14, 16, 2, 0, 109]
mall=0
max=0
print(tb)
for i in range(0,2,n):
    if(max<tb[i]):
        max=tb[i]


print(t[i],". megállóban voltak a legtöbben!")
#c
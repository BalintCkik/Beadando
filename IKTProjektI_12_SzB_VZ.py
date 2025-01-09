import math

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
n=len(tb)
max=0
print(tb)

for i in range(0,n,2):
    if(max<tb[i]):
        max=tb[i]

for i in range(0,n):
    if(tb[i]==max):
        mall=math.ceil((i+1)/2)

print(mall,". megállóban voltak a legtöbben!")

#c
ferohelyek=int(input("Férőhelyek:"))
ferohelyszam=0
for i in range(n):
    if(tb[i]>ferohelyek):
        ferohelyszam+=1
print(ferohelyszam,"megállón keresztül volt álló utas!")

#d
dupla=0
for i in range(n):
    if(tb[i]%ferohelyek==0):
        dupla+=1
if(dupla!=0):
    print("Igen.")
else:
    print("Nem.")
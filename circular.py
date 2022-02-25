a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())
g=[]
h=[]
i=[]
j=[]
es=(2*3.141592653589793)*a/c
g.append(int(es))
ese=es
ess=(2*3.141592653589793)*b/c
h.append(int(ess))
esse=ess 
fs=(2*3.141592653589793)*a/d
i.append(int(fs))
fsf=fs 
fss=(2*3.141592653589793)*b/d
j.append(int(fss))
fssf=fss
while(ese<=e):
  ese+=es
  g.append(int(ese))
while(esse<=e):
  esse+=ess
  h.append(int(esse))
while(fsf<=e):
  fsf+=fs
  i.append(int(fsf))
while(fssf<=e):
  fssf+=fss
  j.append(int(fssf))
cre=0
for iii in g:
  if iii in h:
    cre=int(iii)
crf=0
for jjj in i:
  if jjj in j:
    crf=int(jjj)
    break
if(cre!=0 and crf!=0):
  print(crf,end=' ')
  print("E&F")
  exit()
if(cre!=0):
  print(cre,end=" ")
  print("E",end='')
if(crf!=0):
  print(crf,end=' ')
  print("F")
if(cre==0 and crf==0):
  print("no crash")
'''print(g)
print(h)
print(i)
print(j)'''
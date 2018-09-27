###### this is the second .py file ###########

####### write your code here ##########
st=raw_input("enter the string")
k1=int(input("enter key1="))
k2=int(input("enter key2="))
k3=int(input("enter key3="))
l=len(st)
a1=[]
a2=[]
a3=[]
t=[]
for i in range(l):
   if(st[i]>='a' and st[i]<='i'):
      a1.append(st[i])
   if(st[i]>='j' and st[i]<='r'):
      a2.append(st[i])
   if(st[i]>='s' and st[i]<='z' or st[i]=='_'):
      a3.append(st[i])
print a1
print a2
print a3
a1=(a1[len(a1) -k1:len(a1)]+ a1[0:len(a1) - k1]) 
a2=(a2[len(a2) -k2:len(a2)]+ a2[0:len(a2) - k2])
a3=(a3[len(a3) -k3:len(a3)]+ a3[0:len(a3) - k3])
print a1
print a2
print a3
i=0
j=0
k=0
m=0
for i in range(l):
   if(st[i]>='a' and st[i]<='i'):
      t.append(a1[j])
      j+=1
   if(st[i]>='j' and st[i]<='r'):
      t.append(a2[k])
      k+=1
   if(st[i]>='s' and st[i]<='z' or st[i]=='_'):
      t.append(a3[m])
      m+=1
print t


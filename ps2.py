###### this is the second .py file ###########

####### write your code here ##########
st=raw_input("enter the string")
k1=int(input("enter key1="))
k2=int(input("enter key2="))
k3=int(input("enter key3="))
l=len(st)
import array as arr
a1=array('c',[])
a2=array('c',[])
a3=array('c',[])
for i in range(l):
   if(st[i]>='a' and st[i]<='i'):
      a1.append(st[i])
   if(st(i)>='j' and st(i)<='r'):
      a2.append(st(i))
   if(st(i)>='s' and st(i)<='z' and st(i)=='_'):
      a3.append(st(i))


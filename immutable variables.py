""" IN PYTHON INTEGERS,FLOATS, STRINGS AND TUPLES ARE IMMUTABLE """




str= input ("enter the string : ")
sub=input ("enter the substring : ")
n=int(input("enter the position : "))
empty=[]
for i in range(0,len(str)):
    print(str[i],id(str[i]))
for i in range(0,len(str)):
    empty.append(str[i])
print(empty)
empty.insert(n-1,sub)
str2="".join(empty)
print (str2)
for i in range(0,len(str2)):
    print(str2[i],id(str2[i]))
    
    
    
    #EXAMPLE
"""
enter the string : i  you
enter the substring : love
enter the position : 3
i 3974963296
  3971206688
  3971206688
y 3971206080
o 3971394560
u 3971395008
['i', ' ', ' ', 'y', 'o', 'u']
i love you
i 3974963296
  3971206688
l 3971134784
o 3971394560
v 3971502368
e 3971117248
  3971206688
y 3971206080
o 3971394560
u 3971395008

[Program finished]
"""

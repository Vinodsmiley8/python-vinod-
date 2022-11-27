c=int(input("enter \n 1 : to add string \n 2 : to delete string\n"))

if c==1:

    str= input ("enter the string : ")
    sub=input ("enter the substring : ")
    n=int(input("enter the position : "))
    empty=[]

    for i in range(0,len(str)):
        empty.append(str[i])
    #print(empty)
    empty.insert(n-1,sub)
    str2="".join(empty)
    print (str2)
    
elif c==2:
    
    str= input ("enter the string : ")
    #sub=input ("enter the substring : ")
    n=int(input("enter the position : "))
    h=int(input("number of elements want to pop : "))
    empty=[]

    for i in range(0,len(str)):
        empty.append(str[i])
    #print(empty)
    for i in range(0,h):
        empty.pop(n-1)
    str2="".join(empty)
    print (str2)

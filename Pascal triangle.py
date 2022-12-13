'''

from math import factorial as fact

a=int(input("enter the number of rows :\n"))
 # nCr = n!/((n-r)!*r!) 
for i in range(0,a):
	print("")
	for j in range(0,i+1):
		print(fact(i)//((fact(i-j))*(fact(j))),end=" ")
		j=j+1
	i=i+1
	

'''

''

from math import factorial as fact

a=int(input("enter the number of rows :\n"))
 # nCr = n!/((n-r)!*r!) 
for i in range(0,a):
	print("")
	for k in range(0,a-i):
		print(end=" ")
	
	for j in range(0,i+1):
		print(fact(i)//((fact(i-j))*(fact(j))),end=" ")
		j=j+1
	i=i+1
	
''

a=int(input('enter the number :\n'))
def prime(lower_value,upper_value):
	prime=[]
	for number in range (lower_value, upper_value + 1):  
	    if number > 1:  
	        for i in range (2, number):  
	            if (number % i) == 0:  
	                break  
	        else:  
 	           prime.append(number)
 	           
 	           
	return prime
	
def lcm(number1):
	p=number1
	
	emp=[1]				
	for app1 in prime(1,p):
		for app2 in prime(1,p):
			if number1 % app2 == 0:
				emp.append(app2)
				number1=number1 /app2
			else :
				pass
	print(emp)
	
	
lcm(a)
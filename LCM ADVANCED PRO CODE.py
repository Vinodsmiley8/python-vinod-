from numpy import *
babie=[] 
a=int(input('enter the number of values  :\n'))
########₹#₹₹₹₹₹₹



###₹₹₹₹ function for prime
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
#function return list of factors	           	         
	
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
	return emp
	
#function returns intersection of lists
def common_list_of_lists(lst):
    temp = set(lst[0]).intersection(*lst)
    return list(temp) 
    

#        accept numbers	
pip=[]	
	
for i in range(1,a+1):
	love=int(input("enter the  number   :\n"))
	pip.append(love)
#append all factors lists to one  list 	
fuck=[]	
	
for girl in pip:
	fuck.append(lcm(girl))
	k=len(fuck)
	print("FACTORS OF {} LIST ARE : {} ".format(k,lcm(girl)))

#######MAIN #####
no_lover=1
VINOD=common_list_of_lists(fuck)
for boy in VINOD:
	no_lover=no_lover*boy
	
print("COMMON FACTORS ARE {} AND L.C.M IS  {} ".format(VINOD,no_lover))

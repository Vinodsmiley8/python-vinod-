#code for ascending order of elements in array 
import numpy as np
from math import *
from copy import *

d=np.array([])
a=np.array([1,2,54,29,63,3,8,5,9,44,82,99,1000])
hi=deepcopy(a)

h=len(hi)
for app in range (1,h+1):
  v=min(hi)
  d=np.append(d,v)
  hi=np.delete(hi,np.where(hi==min(hi)))
  
  
print("THE ARRAY U ENTERED :\n",a)
print("THE ARRAY ARRANGED :\n",d)
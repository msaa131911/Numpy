import numpy as np

def myadd(x,y):
    return x+y

ss=np.frompyfunc(myadd,2,1) #frompyfunc(function,inputs,outputs)
print(ss([1,2,3,4],[5,6,7,8]))


#Check if a Function is a ufunc
print(type(np.add))
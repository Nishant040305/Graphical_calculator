from numpy import *
from random import randint

def arcsin(x):
    result=list()
    for elements in range(x.size):
        a="<class 'numpy.float64'>"
        if str(type(emath.arcsin(x[elements])))==a:                
            result.append(emath.arcsin(x[elements]))
        else:
            result.append(0)
    return array(result)
def arccos(x):
    result=list()
    for elements in range(x.size):
        a="<class 'numpy.float64'>"
        if str(type(emath.arccos(x[elements])))==a:                
            result.append(emath.arccos(x[elements]))
        else:
            result.append(0)
    return array(result)
def arctan(x):
    result=list()
    for elements in range(x.size):
        a="<class 'numpy.float64'>"
        if str(type(emath.arcsin(x[elements]/sqrt(x[elements]**2+1))))==a:                
            result.append(emath.arcsin(x[elements]/sqrt(x[elements]**2+1)))
        else:
            result.append(0)
    return array(result)
def arccsc(x):
    result=list()
    for elements in range(x.size):
        a="<class 'numpy.float64'>"
        if str(type(emath.arcsin(1/x[elements])))==a:                
            result.append(emath.arcsin(1/x[elements]))
        else:
            result.append(0)
    return array(result)
def arcsec(x):
    result=list()
    for elements in range(x.size):
        a="<class 'numpy.float64'>"
        if str(type(emath.arccos(1/x[elements])))==a:                
            result.append(emath.arccos(1/x[elements]))
        else:
            result.append(0)
    return array(result)
def arccot(x):
    result=list()
    for elements in range(x.size):
        a="<class 'numpy.float64'>"
        if str(type(emath.arccos(x[elements]/sqrt(x[elements]**2+1))))==a:                
            result.append(emath.arccos(x[elements]/sqrt(x[elements]**2+1)))
        else:
            result.append(0)
    return array(result)

def csc(x):
    return 1/sin(x)
def sec(x):
    return 1/cos(x)
def cot(x):
    return 1/tan(x)
def random(x):
    a = randint(0,x.size-1)
    resut=[x[a] for i in range(x.size)]
    return array(resut)
if __name__=='__main__':
    a = arange(-10,10,0.1)
    print(arctan(a))
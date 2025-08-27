def addition(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def factorial(a):
    factorial=1
    for i in range(2, a+1):
        factorial *= i
    return factorial
def degree(a,b):
    return a**b




vir=input('введите выражение: ')
if "+" in vir:
    v= vir.split('+')
    result = float(v[0])
    for i in range(1,len(v)):
        v[i]=float(v[i])        
        result=addition(result,v[i])
    print(result)
elif "-" in vir:
    v= vir.split('-')
    result = float(v[0])
    for i in range(1,len(v)):
        v[i]=float(v[i])
        result=subtract(result,v[i])
    print(result)
elif "*" in vir:
    v= vir.split('*')
    result = float(v[0])
    for i in range(1,len(v)):
        v[i]=float(v[i])
        result=multiply(result,v[i])
    print(result)
elif "/" in vir:
    v= vir.split('/')
    result = float(v[0])
    for i in range(1,len(v)):
        v[i]=float(v[i])
        result=divide(result,v[i])
    print(result)
elif "!" in vir:
    v= vir.split('!')
    v=v[0].split(' ')
    result=factorial(int(v[-1]))
    print(result)
elif "^" in vir:
    v=vir.split('^')
    result = float(v[0])
    for i in range(1,len(v)):
        v[i]=float(v[i])
        result=degree(result,v[i])
    print(result)
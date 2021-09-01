def dummy (n):
    if n==0:
        return (0)
    if n==1:
        return(1)
    else:
        return (dummy(n-1) + dummy(n-2))

def dummy_better (n):
    result=[]
    result.append(0)
    result.append(1)
    for i in range (1,n+1):
        result.append(result[-2] + result[-1])
    return(result[-2])

def dummy_best(n):
    a=0
    b=1
    for i in range(1, n+1):
        tmp=a
        a=b
        b=tmp+b
    return (a)

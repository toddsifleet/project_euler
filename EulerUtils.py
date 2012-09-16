 #Reusable Code
def getnum(l):
    n=l[0]
    for t in l[1::]: n=n*10+t
    return n

plist = [2]

def Primes(n, x):
    #creates a generator that contains all prime numbers from min to max
    global plist
    if 2 >= n: yield 2
    i = 3
    while i <= x:
        for p in plist:
            if i%p == 0 or p*p > i: break
        if i%p:
            plist.append(i)
            if i >= n: yield i
        i = i+2


def NumFactors(n):
    P=PrimeFactor(n)
    y=1
    for x in set(P[1::]):
        y=y*(1+P.count(x))
    return y

def isPrime(n):
    i=2
    l = n**0.5  
    while i <= l:  
        if n % i == 0:  
            return 0 
        else:  
            i += 1  
    return 1
def PrimeFactor(n):
    n,p,i=abs(n),[1],2
    l = n**0.5  
    while i <= l:  
        if n % i == 0:  
            p.append(i)
            n = n // i  
            l = n**0.5  
        else:  
            i += 1  
    if n > 1:  
        p.append(n)
    return p

def Factor(n):
    from itertools import combinations
    x=list(PrimeFactor(n))
    f=set(x)
    for z in range(2,len(x)):
        for g in combinations(x,z):
            n=1
            for q in g: n=n*q
            f.add(n)
    t=list(f)
    t.sort()
    return t
def Abundant(n,x):
    a=[]
    for i in range(n,x):
        if sum(Factor(i)[0:-1])>i: a.append(i)
    return a
def Deficient(n,x):
    x=[]
    for i in range(n,x)[::-1]:
        if sum(Factor(i)[0:-1])<i: yield i

def isAbundant(n):
    if sum(Factor(n)[0:-1])>n: return True
    else: return False
def PerfectSquares(n,x):
    if n**.5*n==n:yield n
    i=int(n**.5)+1
    while i<=int(x**.5):
        yield i**2
        i+=1
def Reduce(n,d):
    while True:
        for i in PrimeFactor(min(n,d))[::-1]:
            if i==1:return n,d
            if i in PrimeFactor(max(n,d)):
                n=n/i
                d=d/i
                break
def Palandron(n,x,o):
    for i in range(n,x)[::o]:
        if str(i)==str(i)[::-1]:
            yield i
def LCM(a,b):
    if not max(a,b)%min(a,b): return max(a,b)
    l,p=1,{}
    for t in [PrimeFactor(a),PrimeFactor(b)]:
        for i in set(t):
            if i not in p:p[i]=t.count(i)
            else: p[i]=max(p[i],t.count(i))
    for g in p: l=l*g**p[g]
    return l


def TestTime(n,f,*args):
    import time
    s =time.clock()
    for i in xrange(n):
        apply(f,args)
    return (time.clock()-s)*1000/n        

def HandValue(T):
    [h,s]=T
    h.sort(reverse=True)
    Hand,x,y=[1]+h,{},set([])#HIGH CARD
    for i in set(h):
        x[h.count(i)]=i
        y.add(h.count(i))#fxix tghis
    z=len(set(h))
    if z!=len(h):
        if z==4: #OnePair
            return [2,x[2]]+[t for t in h if t!=x[2]]
        elif z==3: #2 Pair or 3 of a kind
            if 3 in y:#3 of a kind
                return [4,x[3]]+[t for t in h if t!=x[3]]
            else: #2 Pair
                h.remove(x[1])
                return [3]+h+[x[1]]
        elif z==2: #Fullhouse or quads
            if 3 in y: return [7,x[3],x[2]]
            else: return [8,x[4],x[1]]
    elif len(set(s))==1: #must have flush
        Hand=[6]+h
    if h[-1]==h[0]-4 or (h[0]==14 and h[1]==5): #straight
        if h[0]==14 and h[1]==5: h=[5,4,3,2,1]
        if Hand[0]==6:return[9]+h
        else: return [5]+h
    return Hand

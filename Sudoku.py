from EulerUtils import getnum
#return possible values for entry n
def Possible(P,n):
    C,B,D,r,c=[],[],set(range(10)),n/9,n%9
    R=[set(P[9*i:9*i+9]) for i in range(0,9)]
    for a in range(0,9):
        C.append(set([P[9*i+a] for i in range(0,9)]))
    for b in [0,3,6,27,30,33,54,57,60]:
        B.append(set(P[b:b+3]+P[b+9:b+12]+P[b+18:b+21]))
    return D-C[c]-B[r/3*3+c/3]-R[r]
#Finds all the easy ones and propogates contstraint
def Constraints(P):
    oldP=[]
    while oldP!=P:
        oldP=P[:]
        for n in range(81):
            if P[n] not in range(1,10):
                s=Possible(P,n)
                if len(s)==1: P[n]=s.pop()
    return P
#loop through and solve it
def Solve(l):
    T=[]
    for i in l:
        P = Constraints(i)
        if P.count(0): n=P.index(0)
        else:
            return P
        for p in Possible(P,n):
            P[n]=p
            T.append(P[:])
    return Solve(T[:])



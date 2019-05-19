import math
def get_corr(n, xsum, ysum, xxsum, yysum, xysum):
    r = ((n*xysum) - (xsum*ysum))/(math.sqrt((n * xxsum) - (xsum**2))*(math.sqrt((n * yysum) - (ysum**2))))

    return r

datalen = int(input())

M = []
P = []
C = []
for i in range(datalen):
    line = input()
    arr = [int(x) for x in line.split('\t')]
    m, p, c = arr[0], arr[1], arr[2]
    M.append(m)
    P.append(p)
    C.append(c)

msum = sum(M)
mmsum = sum([m*m for m in M])
psum = sum(P)
ppsum = sum([p*p for p in P])
csum = sum(C)
ccsum = sum([c*c for c in C])

#m to p
mpsum = sum([x*y for x,y in zip(M,P)])
r1 = get_corr(datalen, msum, psum, mmsum, ppsum, mpsum)
print(round(r1,2))
#p to c
pcsum = sum([x*y for x,y in zip(P,C)])
r2 = get_corr(datalen, psum, csum, ppsum, ccsum, pcsum)
print(round(r2,2))

#c to m
cmsum = sum([x*y for x,y in zip(C,M)])
r3 = get_corr(datalen, csum, msum, ccsum, mmsum, cmsum)
print(round(r3,2))

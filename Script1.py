x=1
L=[]
L.append(x)

def f(x,L=[2]):
        x=2*x
        L.append(x)
        print L,x
        
f(x)
print "f(x):",L,x

f(x,L)
print "f(x,L):",L,x
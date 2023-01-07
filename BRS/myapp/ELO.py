def elo(p1,p2,p3,p4,k1,k2,k3,k4):
    
    
    k1=constant(k1)
    k2=constant(k2)
    k3=constant(k3)
    k4=constant(k4)
    
    ta = p1+p2
    tb = p3+p4
    x=(tb-ta)/400   
    y=pow(10,x)
    PTa=1/(1+y)
    PTb=1-PTa

    p1=p1+k1*(1-PTa)
    p2=p2+k2*(1-PTa)         
    p3=p3+k3*(0-PTb)         
    p4=p4+k4*(0-PTb)         	
 
    ratings = [p1,p2,p3,p4]
    return ratings 


def constant(n):
    k= 55-n
    if(k <10):
        k=10
    return k

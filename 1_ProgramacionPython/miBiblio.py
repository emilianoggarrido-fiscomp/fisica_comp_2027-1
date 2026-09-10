def dist(r,t,z):
    """Calcula la distancia del origen al punto p (con coordenadas
    (r,t,z) cilindricas).
    """
    import math as mt
    return mt.sqrt(r**2 + z**2)

def fact(n):
    """Regresa el factorial de n.
    """
    f_n = 1
    for i in range(1,n+1):
        f_n = f_n*i
    return f_n

def fact(n):
    """Regresa el factorial de n de forma recursiva.
    """
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)

def cat(n):
    """Regresa el n-esimo numero de Catalan calculandolo de forma recursiva.
    """
    if n == 0:
        return 1
    return ( (4*(n-1)+2) / ((n-1)+2) )*cat(n-1)

def mcd(m,n):
    """Regresa el maximo comun divisor de la pareja (m,n) """
    if n==0:
        return m
    return mcd(n,m%n)

def fact_prim(x):
    """ Regresa una lista de los factores primos de x """
    p = []
    n=2
    while n*n<=x:
        while (x%n)==0:
            p.append(n)
            x //= n
        n += 1
    if x>1:
        p.append(x)
    return p

def list_prims(x):
    c = []
    for n in range(2, x+1):
        if len(fact_prim(n))==1:
            c.append(n)
    return c
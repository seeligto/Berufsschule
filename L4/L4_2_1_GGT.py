def ggT(a, b):
    m=a
    n=b
    
    if m < n:
        m, n = n, m
    
    r=m-n
    m, n = n, r
    
    while r !=0:
        if m < n:
            m, n = n, m
        r=m-n
        m, n = n, r
    
    return m

a = int(input("Zahl a"))
b = int(input("Zahl b"))

print("Kleinster Teiler ist: ", ggT(a, b))
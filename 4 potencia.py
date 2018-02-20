def potencia(a,b):
    if b==0:
        return 1
    if b==1:
        return a
    return a*potencia(a,b-1)

print (potencia(5,2))


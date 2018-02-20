import math

def sumatoria(n):
    if n==0:
        return 0;
    if n==1:
        return 1;
    return(n%10+(sumatoria(math.floor(n/10))))

print(sumatoria(901))

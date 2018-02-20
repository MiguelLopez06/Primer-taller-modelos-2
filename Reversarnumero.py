def rev(n):
    def rec(n, diez):
        if n < 10:
            return n
        else:
            return n % 10 * diez + rec(n // 10, diez // 10)  
    return rec(n, 10 ** (cont(n)-1))

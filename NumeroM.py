def big(n):
    def rec(n, diez):
        if n < 10:
            return n
        else:
            if (n % 10 >= rec(n // 10, diez // 10)):
                return n % 10
            elif(n % 10 <= rec(n // 10, diez // 10)):
                return rec(n // 10, diez // 10)
    return rec(n,  10 ** (cont(n)-1))


print(big(int(input(465786))))

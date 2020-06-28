def rec(n):
    if n > 0:
        rec(n-1)
        rec(n-1)
        print("Print : ", n)
    

rec(3)
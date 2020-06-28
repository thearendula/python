def rec(n):
    if n > 0:
        print("Print : ", n)
        rec(n-1)
        print("Print : ", n)
    

rec(3)
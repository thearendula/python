def rec(n):
    if n > 0:
        rec(n-1)
        print("Sid", n)
        rec(n-1)
    

rec(4)
def rec(n):
    if n > 0:
        print("Sid", n)
        rec(n-1)
        rec(n-1)
    

rec(3)
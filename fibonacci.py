def fib(n):
    if n <= 1:
        return n
    else:
        return (fib(n-1) + fib(n-2))


count = 10
if count <= 0:
    print("Minimum value")
else:
    for i in range(count):
        print(fib(i), end=" ")

 

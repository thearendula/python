def fact(n):
    if n == 1 or n == 0:
        return 1
    elif n < 0:
        print("Number should not be less than zero")
    else:
        return n * fact(n - 1)


num = input("Enter the number : ")
num = int(num)
print(fact(num))
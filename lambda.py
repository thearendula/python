# def is__even(n):
#     return n%2==0

# nums = [5,6,3,2,7,9,8,4,2,4,2,5,45,2,84,5,15]
# evens = list(filter(is__even, nums))
# print(evens)

#Alternative using lambda function

nums = [5,6,3,2,7,9,8,4,2,4,2,5,45,2,84,5,15]
evens = list(filter(lambda n : n%2!=0, nums))
print(evens)
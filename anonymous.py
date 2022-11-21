from functools import reduce
nums = [2,3,4,5,6,7,8,9,10,11]
evens = set(filter(lambda n : n%2==0,nums))
doubles = list(map(lambda n : n*n,evens))
for i in doubles:
    print(i+1)
sum = reduce(lambda a,b : a+b,doubles)



print(evens)
print(doubles)
print(sum)
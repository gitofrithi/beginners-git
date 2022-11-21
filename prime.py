minimum = int(input('enter minimum number:'))
maximum = int(input('enter maximum number'))
for number in range(minimum,maximum+1):
    count=0
    for i in range(2,number):
        if number%i==0:
            count=count+1
            break
    if count==0 and number!=1:
        print(number,end='')
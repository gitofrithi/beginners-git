a = 5
b = 0
try:
    print('resources open')
    k = int(input('enter a number'))
    print(k)
    print(a/b)

except ZeroDivisionError as e:
    print('he you cannot divide a number by zero',e)
except ValueError as e:
    print('invalid input')
except Exception as e:
    print('invalid error')
finally:
    print('resource closed')
print('bye')

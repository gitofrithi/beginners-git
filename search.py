print('lenear search')
pos = -1
def search(list,n):
    i = 0
    for i in list:
        if list[i] == n:
            globals()['pos'] = i
            return True
        return False

list = [1,2,3,4,5,6,7,8]
n = 5
if search(list,n):
    print('found at',pos)
else:
    print('not found')


print('Binary sorted search')

pos = -1
def search(list,n):
    l = 0
    u = len(list)-1
    while l <= u:
        mid = (l+u) // 2

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid
            else:
                u = mid

list = [1,2,3,4,5,6,7,8,9,10]
n = 9
if search(list,n):
    print('found at',pos)
else:
    print('not found')


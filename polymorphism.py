print('duck typing')
class Pycharm:
    def execute(self):
        print('compiling')
        print('runnimg')
class Mycharm:
    def execute(self):
        print('spell check')
        print('convenction check')
        print('compiling')
        print('running')
class laptop:
    def code(self,ide):
        ide.execute()
ide =Mycharm()
lap1 = laptop()
lap1.code(ide)

print('operator overloading')
class student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = student(m1,m2)
        return s3
    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False
    def __str__(self):
        return '{} {}'.format(s1.m1,s2.m2)
s1 = student(10,30)
s2 = student(20,10)
s3 = s1 + s2
print(s3.m1,s3.m2)
if s1 > s2:
    print('s1 wins')
else:
    print('s2 wins')
print(s1)
print(s2)

print('method overloading')
class student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def sum(self,a = None,b = None ,c = None):
        s = 0
        if a!=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a+b
        else:
            s = a
        return s
s1 = student(11,12)
print(s1.sum(1,2,3))

print('method overriding')

class A:
    def show(self):
        print('its A show')
class B(A):
    def show(self):
        print('its B show')

r = B()
print(r.show())


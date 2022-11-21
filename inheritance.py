class A:
    def __init__(self):
        print('this is a class')
    def feature1(self):
        print('feature 1 is working')
    def feature2(self):
        print('feature 2 is working')
class B():
    def __init__(self):
        super().__init__()
        print('this is b class')
    def feature3(self):
        print('feature 3 is working')
    def feature4(self):
        print('feature 4 is working')
class C(B,A):
    def __init__(self):
        super().__init__()
        print('this is c class')

c1 = C()





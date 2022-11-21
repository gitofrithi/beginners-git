from abc import ABC, abstractmethod

class computer(ABC):
    @abstractmethod
    def process(self):
        pass
class laptop(computer):
    def process(self):
        print('its running')
class whiteboard(computer):
    def write(self):
        print('its writing')
class programmer:
    def work(self,com):
        print('solving bugs')
        com.process()

#comp = computer()
com1 = laptop()
com2 = whiteboard()
#comp.process()
prog1 = programmer()
prog1.work(com2)
class hi:
    def __init__(self, st='some thing'):
        self.s = st

    def sayhello(self):
        print('hello')

    def saybye(self):
        print('bye')

    def saySth(self):
        print(self.s)

    def setSth(self, st):
        self.s = st


h = hi()
h.sayhello()
h.saybye()
h.saySth()
h.setSth('changed')
h.saySth()
b = hi('fda')
b.saySth()

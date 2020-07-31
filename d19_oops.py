class X:
    def m(self):
        self.a=1000
        self.b=2000
    def n(self):
        print(self.b)
x=X()
x.m()
print(x.a)
x.n()

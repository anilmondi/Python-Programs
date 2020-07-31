class A:
     def m(self):
          print("a")
class B(A):
     def n(self):
          print("Two")
class C(A):
     pass
o=C()
o.m()
p=B()
p.n()
p.m()

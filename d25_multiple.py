class A:
     def m(self):
          print("one")
class B:
     def n(self):
          print("two")
class C(A,B):
     def o(self):
          print("Three")
o=C()
o.m()
o.n()
o.o()

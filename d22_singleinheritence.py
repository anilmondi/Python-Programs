class A:
     def m(self):
          print("I am from class A")
class B(A):
     def n(self):
          print("I am from class B")
o=B()
o.m()
o.n()

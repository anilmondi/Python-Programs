class A:
     def x(self):
          print("I am from class A")
class B(A):
     def y(self):
          print("I am from class B")
class C(B):
     def z(self):
          print("I am from class C")
class D(C):
     pass
o=D()
o.x()
o.y()
o.z()

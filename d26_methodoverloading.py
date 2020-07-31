class methodoverloading:
     def m1(self):
          print("I am one arguement")
     def m1(self,a):
          print("I am three arguements")
     def ma(self,a,b):
          print("I am three arguements")
o=methodoverloading()
o.m1(10)

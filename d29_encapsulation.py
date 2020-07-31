#encapsulation N=Normal M=Method
class N:
     __a=3 #__ is make the variable a is private
     b=5
     def __pnm(self):               #__ is private method
          print("accessed only here",self.__a)
          print("i am private method")
     def nm(self):
          print("i am normal method")
          self.__pnm()        #we can access the private variables and methods within the class
o=N()
o.nm()
#print(o.a)->it cannot access outside the class 
print(o.b)

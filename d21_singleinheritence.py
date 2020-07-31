class A:
    def m(self):
        print("i'm class A")
class B(A):
    pass
object=B()
object.m()

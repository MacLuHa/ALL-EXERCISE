class Share():
    def what_i_am(self):
        print("Я-фигура!")
        
class Rectangle(Share):
    def __init__(self,a,b):
        self.widht=a
        self.len=b
    def calculate_perimeter(self):
        return 2*(self.widht+self.len)

class Square(Share):
    def __init__(self,a):
        self.side=a
    def change_size(self,n):
        self.side+=n

square=Square(3)
rectangle=Rectangle(3,5)
rectangle.what_i_am()
square.what_i_am()

class Square:
    def __init__(self,a):
        self.side=a
    def change_size(self,n):
        self.side+=n
a_square=Square(100)
print(a_square.side)
a_square.change_size(200)
print(a_square.side)

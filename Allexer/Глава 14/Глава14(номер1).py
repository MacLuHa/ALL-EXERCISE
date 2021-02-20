class Square():
    square_list=[]
    def __init__(self,s,r):
        self.size=s
        self.radius=r
        self.square_list.append((self.size,self.radius))
    def per(self):
        return self.size**2
sq=Square(3,2)
sq2=Square(3,5)
sq3=Square(4,2)
print(Square.square_list)
print(sq.per())
print(sq2.per())
print(sq3.per())

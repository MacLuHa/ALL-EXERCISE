class Square:
    square_list=[]
    def __init__(self,size):
        self.size=size
        self.square_list.append((self.size))
    def __repr__(self): #Как оказалось,можно создать эту функцию и так,без print,а просто вписав в return
        return ("""{} на {} на {} на {}
              """.format(self.size,self.size,self.size,self.size))
sq=Square(29)
sq1=Square(30)
sq2=Square(2)
print(sq)
print(sq1)
print(sq2)


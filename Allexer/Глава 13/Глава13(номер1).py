class Rectangle:
    def __init__(self,a,b):
        self.widht=a
        self.len=b
    def calculate_perimeter(self):
        return 2*(self.widht+self.len)
class Square(Rectangle):    #Создаем дочерний класс Square(переменные класса Rectangle передаются новому классу)
    pass                  #pass-ключевое слово,сообщающее Python ничего не делать
rectangle=Rectangle(20,30)
square=Square(22,22)

print("Периметр прямоугольника равен",rectangle.calculate_perimeter())
print("Периметр квадрата равен",square.calculate_perimeter())

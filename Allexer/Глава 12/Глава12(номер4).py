class Hexagon:
    def __init__ (self,s,n):
        self.storona=s #назначаем переменные экземпляра
        self.numbers=n
    def calculate_perimeter(self): #данный метод оперирует переменными экземпляра
        return self.storona*self.numbers  #ищем периметр шестиугольника

hexagon=Hexagon(8,6)
print(hexagon.calculate_perimeter()) #выводим значение периметра


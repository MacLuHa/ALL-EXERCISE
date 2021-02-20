class Triangle:
    def __init__(self,h,b):  #Ввели переменные
        self.base=b          #переменные экземпляра
        self.height=h
    def area(self):        #данный метод оперирует переменными экземпляра
        return (self.base*self.height)/2

triangle=Triangle(14,20)
print("S данного треугольника равна",triangle.area())

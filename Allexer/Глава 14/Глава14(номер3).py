class Cat:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
    def srav(self,other_name,other_breed):
        if self.name==other_name:
            if self.breed==other_breed:
                return True
            return True
        else:
            return False
cat1=Cat("Mike","Tiger")
cat2=Cat("Nike","Puma")
cat3=Cat("Mike","Tiger")
print(cat1.srav("Mike","erwwg")) #Переменные в скобках и есть other_name и other_breed
                                 #метод srav сравнивает их с объктом,стоящим перед скобкой



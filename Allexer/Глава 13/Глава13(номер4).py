class Horse():
    def __init__(self,c,y,r):
        self.color=c
        self.year=y
        self.rider=r
class Rider():
    def __init__(self,n):
        self.name=n

ya=Rider("Максим Шухтуев")
horse=Horse("Чёрный",13,ya)
print("Всадником лощади является {}".format(horse.rider.name))

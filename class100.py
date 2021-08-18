class class100(object):
    def __init__(self,brand,wheels,chasis,speedlimit,color):
        self.brand=brand
        self.wheels=wheels
        self.chasis=chasis
        self.speedLimit=speedlimit
        self.color=color
    def company(self):
        print('MERCEDES')
    def tyre(self):
        print('4 offroad')
    def body(self):
        print('Metal chasis')
    def maxSpeed(self):
        print('150 miles per hour')
        
class1001=class100('MG','4 offroad','Metal chasis','150 miles per hour','blue')
print(class1001.company())
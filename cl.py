class Car(object):
    def __init__(self,color,model,company):
        self.color = color
        self.model = model
        self.company = company
    def start(self):
        print("started")
    def stop(self,time):
        print(time)

car = Car("red","BMW","Tata")
car.stop("time")
print(car.company)
class Vehicle:
    def __init__(self,seat):
        self.seat=seat
        self.maintenance_charge=0.10*seat
        self.fare_price=seat*100+self.maintenance_charge

    def display(self):
        print("The fare price is", self.fare_price)

class Bus(Vehicle):
    def __init__(self,seat):
        Vehicle.__init__(self,seat)


obj=Bus(50)
obj.display()
    


     

        
#Working on the car object

class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg
	def display_car(self):
		#Note that have to use self within the method display_car so that it knows to what the method refers
		return "This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg))
		#Note that here have to use self. to call the member variables, even within the class
	
	def drive_car(self):
        self.condition = "used"
		
my_car = Car("DeLorean", "silver", 88)
#print my_car.condition
#print my_car.model
#print my_car.color
#print my_car.mpg
#print my_car.display_car()

print my_car.condition
my_car.drive_car()
print my_car.condition

class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
        self.model = model
        self.color = color
        self.mpg   = mpg
        self.battery_type = battery_type
	
	def drive_car(self):
        self.condition = "like new"
 
my_car2 = ElectricCar("DeLorean", "silver", 88, "molten salt")
print my_car2.condition
my_car2.drive_car()
print my_car2.condition
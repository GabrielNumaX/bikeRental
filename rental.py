#Customer
#see available bikes
#rent per hour $5
#rent per day $20
#rent per week $60
#family rental, 3 to 5 rentals (any type) 30% discount total price

#Rental shop
#bill when customer returns bike
#display inventory
#take requests on hour, day, week by verifying stock

class Rental:

	bikes=100

	@classmethod
	def checkBikes(cls):
		return "There are {} bikes in stock".format(cls.bikes)

	def __init__(self, customerName, rentalType, rentalQty, family=False, bill=None):
		self.customerName=customerName
		self.rentalType=rentalType
		self.rentalQty=rentalQty
		self.family=family
		self.bill=bill

		Rental.bikes -= self.rentalQty
		self.checkFamily()


	def checkFamily(self):
		if self.rentalQty >= 3 and self.rentalQty <= 5:
			self.family = True
 

	def rentalBill(self):
		if self.rentalType == "hour" and self.family == False:
			bill = self.rentalQty * 5
			Rental.bikes += self.rentalQty
			return "{}'s bill is ${}.".format(self.customerName, bill)

		elif self.rentalType == "day" and self.family == False:
			bill = self.rentalQty * 20
			return "{}'s bill is ${}.".format(self.customerName, bill)

		elif self.rentalType == "week" and self.family == False:
			bill = self.rentalQty * 60
			return "{}'s bill is ${}.".format(self.customerName, bill)

		elif self.rentalType == "hour" and self.family == True:
			bill = (self.rentalQty * 5) * 0.7
			return "{}'s bill is ${}.".format(self.customerName, bill)

		elif self.rentalType == "day" and self.family == True:
			bill = (self.rentalQty * 20) * 0.7
			return "{}'s bill is ${}.".format(self.customerName, bill)

		elif self.rentalType == "week" and self.family == True:
			bill = (self.rentalQty * 60) * 0.7
			return "{}'s bill is ${}.".format(self.customerName, bill)

		else:
			return "There's an error, checked input data"

		#I did the rentalBill with it's conditions first
		#then I implemented checkFamily to set true or false

		#when I try to execute this method it gives me an error see line 105
		def takeRequest(self, name, request, requestType):
			if request > Rental.bikes:
				Rental.bikes -= request
				self.customerName = name
				self.rentalQty=request
				self.rentalType = requestType

				return "{}'s requests {} bikes on {} rate".format(name, request, requestType)
			else:
				return "Not enough bikes to process request"

		

customer1=Rental("gabo", "hour", 2)

customer2=Rental("juan", "day", 3)

customer3=Rental("pedro", "week", 6)

print(customer1.customerName,customer1.rentalType ,customer1.rentalQty)

print(Rental.checkBikes())

print(customer1.rentalBill())

print(Rental.checkBikes())

print(customer2.rentalBill())

print(Rental.checkBikes())

print(customer3.rentalBill())

print(Rental.checkBikes())

#print(customer3.takeRequest("pedro", 20, "hour"))
#when I execute this I get the following error 
#AttributeError: 'Rental' object has no attribute 'takeRequest'
#Don't undertand why?


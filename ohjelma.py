# Basket is a simple class for a MVP stage shopping application
# You can make a new basket by adding a name, list of products and a price
# You can return the name of the customer, the contents of the basket and the price
# You can add items later as well
# You can count the new price if you have a discount

# TODO: exception handling, user input...

class Basket:
	def __init__(self, customer, contents, price, alv, productAmount, averagePrice):
		self.customer = customer
		self.contents = contents
		self.price = price
		self.alv = alv
		self.productAmount = productAmount
		self.averagePrice = averagePrice

	def return_customer(self):
		return self.customer

	def return_contents(self):
		return self.contents

	def return_price(self):
		return self.price

	def return_alv(self):
		return self.alv
		
	def return_productAmount(self):
		return self.productAmount
		
	def return_averagePrice(self):
		return self.averagePrice

	def add_product(self, product, product_price):
		self.contents.append(product)
		self.price += product_price

	def delete_product(self, product, product_price):
		for i in self.contents:
			if i == product:
				self.contents.remove(product)
				self.price -= product_price

	def count_discount_price(self, percent):
		discount = percent / 100.0
		return self.price - self.price * discount

	def count_price_without_alv(self, price):
		alv = 0.24
		return self.price - self.price * alv
		
	def count_productAmount(self, productAmount):
		productAmount = len(self.contents)
		return self.productAmount
		
	def count_average_price(self, averagePrice):
		averagePrice = self.price / len(self.contents)
		return averagePrice
		

# Making a test object:
# jarin_ostoskori = Basket("Jari", ["maito","banaani","hernekeitto"], 15)


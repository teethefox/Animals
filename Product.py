class Product(object):
  def __init__(self, price, item_name, weight, brand, cost, sell):
    self.price = price
    self.item_name = item_name
    self.weight = weight
    self.brand = brand
    self.cost = cost
    self.sell = sell
  def status(self,status):
    self.status = status
    
    print status
  def add_tax(self, tax):
    tax = 0.8
    self.price = self.price - self.price * tax
    return self.price
  def Return(self, reason):
    if reason is str("defective"):
      self.price = 0
      print "The new price is",self.price
      print "Current status is:"
      shirt.status=shirt.status("defective")
    elif reason is str("inbox"):
      print "Current status is:",
      shirt.status= shirt.status("for sale")
    elif reason is str("openbox"):
      print "Current status is:",
      shirt.status = shirt.status("used"), 
      print "Discounted price is:", self.price - self.price * 0.20
      return self
    def sell(self):
      shirt.sell = "sold"
  def displayInfo(self):
    print "Brand:", shirt.brand, ",Price:" ,shirt.price, ",", "Status:", shirt.sell, ",Weight:", shirt.weight, ",Cost of prodction in dollars:" , shirt.cost, ',Item Name:' , shirt.item_name
  
shirt = Product(100,"shirt","20lbs","Fox", 200, "sold")
shirt.displayInfo()
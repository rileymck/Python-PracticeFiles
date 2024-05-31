class User:
  
  def __init__(self, firstName, lastName, age, color, animal):
    self.first = firstName
    self.last = lastName
    self.age = age
    self.color = color
    self.animal = animal
    
    #First Name
  def get_fisrtName(self):
    return self.first 
  def set_firstName(self, firstName):
    self.first = firstName
    
    #Last Name
  def get_lastName(self):
    return self.last 
  def set_lastName(self, lastName):
    self.last = lastName
    
    #Age
  def get_Age(self):
    return self.age 
  def set_Age(self, age):
    self.age = age  
  
    #Color
  def get_Color(self):
    return self.color 
  def set_Color(self, color):
    self.color = color   
   
    #Animal
  def get_Animal(self):
    return self.animal 
  def set_Animal(self, animal):
    self.animal = animal 
  
  def DescribeUser(self):
    return self.first, self.last, self.age, self.color, self.animal
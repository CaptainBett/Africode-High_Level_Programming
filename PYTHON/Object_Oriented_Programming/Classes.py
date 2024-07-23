# class Person:
#     def __init__(self, name,id,age):
#        self.name = name
#        self.age = age
#        self.id = id

#     def introduce(self):
#         print(f'My name is {self.name}(ID no:{self.id}).I am {self.age} years old.')

# teacher = Person("Ben", "35789980", 30)
# teacher.introduce()

# class Student(Person):
#     def study(self):
#         print(f"{self.name} is studying.He is admission {self.id} and {self.age}yrs of age.")
        
# student = Student("Enock","002",18)
# student.study()
    
# class Teacher(Person):
#     def teach(self):
#       print(f'{self.name} is teaching.His ID is {self.id} and is {self.age}.')

# teacher = Teacher("Ben", "001", 30)
# teacher.teach()
















class Vehicle:
    def __init__(self,color,year,company):
       self.color = color
       self.company = company
       self.year = year

    def myCar(self):
        print( f'I own a {self.color} {self.year} {self.company}.')

car = Vehicle("blue",2018,"BMW")  
lorry = Vehicle("white",2016,"Mercedes")
car.myCar()
lorry.myCar()
# car = Vehicle("blue",2018,'BMW')
# car.myCar()


# class Bike(Vehicle):
#     def type(self):
#         print(f'Benz has a {self.color} {self.company} that was first released in May {self.year}!')

# motorbike = Bike('golden','Kawasaki ninja',2022)
# motorbike.type()





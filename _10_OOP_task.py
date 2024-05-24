#1 
class rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
        
        
    def area(self):
        return f"area is : {self.width * self.length}"
        
class parallelograms(rectangle):
    def __init__(self, width, length, height):
        self.width = width
        self.length = length
        self.height = height
        
    def par_area(self):
        return f" parallelograms area is : {(2 * self.width * self.length) + (2 * self.length * self.height) + (2 * self.width * self.height)}" 
        
obj_1 = rectangle(5, 8)
print(obj_1.area())
obj_1 = parallelograms(5, 8, 10)
print(obj_1.par_area())


#2 

class bachelor:
    def __init__(self, surname, name, course):
        self.surname = surname
        self.name = name
        self.course = course
        
    def disp_info(self):
        print(f"surname : {self.surname}")
        print(f"name : {self.name}")
        print(f"course : {self.course}")
        
        
class master(bachelor):
    def __init__(self, surname, name, course, devops):
        bachelor.__init__(self,surname, name, course)
        self.devops = devops
        
    def disp_info_master(self):
        print(f"surname : {self.surname}")
        print(f"name : {self.name}")
        print(f"course : {self.course}")
        print(f"Theme of Master : {self.devops}")
        
class doctoral(master):
    def __init__(self, surname, name, course, devops, published_papers_quantity):
        master.__init__(self,surname, name, course, devops)
        self.published_papers_quantity = published_papers_quantity

    def disp_info_doctoral(self):
        print(f"surname : {self.surname}")
        print(f"name : {self.name}")
        print(f"course : {self.course}")
        print(f"Theme of Master : {self.devops}")
        print(f"Published Papers Quantity : {self.published_papers_quantity}")


obj_2 = bachelor("Garcia", "Luis", "Information Technology\n")
obj_2.disp_info()
obj_3 = master("Garcia", "Luis", "Information Technology", "DevOps\n")
obj_3.disp_info_master()
###print(issubclass(master,bachelor))
obj_4 = doctoral("Garcia", "Luis", "Information Technology", "DevOps",3)
obj_4.disp_info_doctoral()
### print(issubclass(doctoral,master))
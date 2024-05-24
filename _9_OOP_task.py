
#1

class tanamshromeli:
    def __init__(self, surname, name, age, work_experience, wage):
        self.surname = surname
        self.name = name
        self.age = age
        self.work_experience = work_experience
        self.wage = wage

    def display_info(self):
        print(f"Name: {self.surname}")
        print(f"Species : {self.name }")
        print(f"age : {self.age}")
        print(f"work experience : {self.work_experience}")
        print(f"wage : {self.wage}")


    

obieqti = tanamshromeli("Cage", "Johnny", 35, 5, 3500)
obieqti.display_info()


#2 

class studenti:
    def __init__(self,surname, name, math, english, science):
        self.surname = surname
        self.name = name
        self.math = math
        self.english = english
        self.science = science

 
    def display_info(self):
        print(f"surname: {self.surname}")
        print(f"name : {self.name }")
        print(f"math : {self.math}")
        print(f"english : {self.english}")
        print(f"science : {self.science}")


    def avrg_score(self):
        return f"average score is : {(self.math + self.english + self.science) / 3}"

obieqti2 = studenti("Johnson", "Adam", 61, 77, 55)
obieqti2.display_info()
print(obieqti2.avrg_score())
        
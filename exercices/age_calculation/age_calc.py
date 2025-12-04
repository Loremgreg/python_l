from datetime import date
class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date = date_of_birth

    def __str__(self):
        return f"{self.name} is from {self.country}, he is born in {self.date}" 
    
    def calc_age(self):
        today = date.today()
        birth = self.date
        age = today.year - birth.year
        return age

    @staticmethod
    def get_birth():
        user_question = input("Date of Birth (YYYY-MM-DD): ")
        birth_date =date.fromisoformat(user_question)
        return birth_date

born = Person.get_birth() 
p1 = Person("Paul", "Belgium", born)
print(p1)
age = p1.calc_age()
print(f"Age: {age}")


# Write a Python program to create a person class. Include attributes like name, country and date of birth. 
# Implement a method to determine the person's age.

# https://www.w3resource.com/python-exercises/oop/python-oop-exercise-2.php
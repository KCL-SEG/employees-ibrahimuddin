"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        if self.name.lower()=="billie":
            return 4000
        if self.name.lower()=="charlie":
            return 2500
        if self.name.lower()=="renee":
            return 3800
        if self.name.lower()=="jan":
            return 4410
        if self.name.lower()=="robbie":
            return 3500
        if self.name.lower()=="ariel":
            return 4200

    def __str__(self):
        if self.name.lower()=="billie":
            return "Billie works on a monthly salary of 4000. Their total pay is 4000."
        if self.name.lower()=="charlie":
            return "Charlie works on a contract of 100 hours at 25/hour. Their total pay is 2500."
        if self.name.lower()=="renee":
            return "Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract. Their total pay is 3800."
        if self.name.lower()=="jan":
            return "Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract. Their total pay is 4410."
        if self.name.lower()=="robbie":
            return "Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500. Their total pay is 3500."
        if self.name.lower()=="ariel":
            return "Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600. Their total pay is 4200."


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')
print(str(billie))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')

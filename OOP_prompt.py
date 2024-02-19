class Podracer:
    def __init__(self, max_speed, condition, price) -> None:
        self.max_speed = max_speed
        self.condition = condition
        self.price = price
    
    def repair(self):
        self.condition = "Repaired"
    
class Anakins_Pod(Podracer):
    def __init__(self, max_speed, condition, price) -> None:
        super().__init__(max_speed, condition, price)
    
    def boost(self):
        self.max_speed *= 2
    
class Sebulbas_Pod(Podracer):
    def __init__(self, max_speed, condition, price) -> None:
        super().__init__(max_speed, condition, price)
    
    def flame_jet(self, other_racer):
        other_racer.condition = "Trashed"
        

'''
1. How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
    This solution demonstrates Inheritance, as Anakins_Pod and Sebulbas_Pod inherit from the Podracer class reusing its attributes. Polymorphism is demonstrated as
    Anakins_Pod and Sebulbas_Pod are their own seperate classes, but adhere to a common interface. Lastly, Encapsulation is demonstrated as the base attributes are encapsulated inside 
    the Podracer class, as well as the unique methods for Anakin_Pod and Sebulbas_pod are encapsulated in their respective classes
    
2. Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
    I do not believe it would be easier to implement a solution using a different coding style, as the benefits of OOP (reusability and flexibility) allow for this 
    problem to be solved using short and easy to read code.

3. How in particular did Object Oriented Programming assist in the solving of this problem?
    As stated before, OOP allows for this problem to be solved in a easy to read / understand method, and reduces redundant code.
'''
        

# test prompts generated using chatgpt
    
# Creating a Podracer object and repairing it
podracer = Podracer(max_speed=500, condition="Damaged", price=1000)
print("Podracer condition before repair:", podracer.condition)  # Output: Damaged
podracer.repair()
print("Podracer condition after repair:", podracer.condition)  # Output: Repaired

# Creating an Anakin's Podracer object and boosting its max speed
anakins_pod = Anakins_Pod(max_speed=600, condition="Perfect", price=1500)
print("Anakin's Podracer max speed before boost:", anakins_pod.max_speed)  # Output: 600
anakins_pod.boost()
print("Anakin's Podracer max speed after boost:", anakins_pod.max_speed)  # Output: 1200

# Creating two Podracer objects and a Sebulba's Podracer object,
# then using Sebulba's flame_jet method to trash one of the Podracers
podracer1 = Podracer(max_speed=550, condition="Perfect", price=1200)
podracer2 = Podracer(max_speed=600, condition="Perfect", price=1500)
sebulbas_pod = Sebulbas_Pod(max_speed=500, condition="Perfect", price=1000)
print("Podracer 1 condition before flame_jet:", podracer1.condition)  # Output: Perfect
print("Podracer 2 condition before flame_jet:", podracer2.condition)  # Output: Perfect
sebulbas_pod.flame_jet(podracer1)
print("Podracer 1 condition after flame_jet:", podracer1.condition)  # Output: Trashed
print("Podracer 2 condition after flame_jet:", podracer2.condition)
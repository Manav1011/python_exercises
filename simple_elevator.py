import time
import humanize
from os import system
class elevator:
    lift_current=0
    status=False
    
    @staticmethod
    def is_working():
        elevator.status=True
        
    def __init__(self,name):
        self.name = name
        
    def elevator_system(self):
        if elevator.status:
            print("Heyy {} to which floor you want to go".format(self.name))
            print("The lift is on {} Floor currently".format(humanize.ordinal(elevator.lift_current)))
            user_str=input("Which floor are you on currently: ")
            
            if not user_str.isdigit():
                system("cls")
                print("Please enter a valid floor number!!")
                elevator.elevator_system(self)
            
            else:
                user=int(user_str)
                if not 0<=user<=9 :
                    print("Floor number must be between 0 and 9")
                    system("cls")
                    self.elevator_system()
                else:
                    old=elevator.lift_current
                    elevator.lift_current =int(user)
                    new=elevator.lift_current
                    system("cls")
                    print(f"lift is coming to {humanize.ordinal(elevator.lift_current)} floor")
            
                    if old>new:
                        time.sleep(old-new)
                        print(f"The lift is on {humanize.ordinal(elevator.lift_current)} Floor currently")
                    elif old<new:
                        time.sleep(new-old)
                        print(f"The lift is here on  {humanize.ordinal(elevator.lift_current)} Floor to take you!!")
                    else:
                        print(f"The lift is on {humanize.ordinal(elevator.lift_current)} Floor currently")
                    y_or_n=str(input("Do you wanna go to another floor[y/n]: "))
            
                    if y_or_n=="y":
                        system("cls")
                        elevator.elevator_system(self)
                    else:
                        system("cls")
        
        else:
            print("The lift is currently not working")
            
elevator.is_working()

user1=elevator("manav")
user1.elevator_system()

        
    
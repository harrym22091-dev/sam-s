#sams sandwhich task
def bread_selection():
    bread_list = ["White", "Brown", "Italian", "Granary"]
    count=0
    print("We have the following breads:")
    while count < len(bread_list):
        print(count+1," ", bread_list[count])
        count += 1
    bread_selected=int(input("which bread did you want? Enter a number: "))
    return bread_list[bread_selected-1]

def Meat_selection():
    Meat_list = ["Ham", "Beef", "Chicken", "lamb"]
    count=0
    print("We have the following breads:")
    while count < len(Meat_list):
        print(count+1," ", Meat_list[count])
        count += 1
    Meat_selection=int(input("which bread did you want? Enter a number: "))
    return Meat_list[Meat_selection-1]

def Meat_selection():
    Meat_list = ["Ham", "Beef", "Chicken", "lamb"]
    count=0
    print("We have the following breads:")
    while count < len(Meat_list):
        print(count+1," ", Meat_list[count])
        count += 1
    Meat_selection=int(input("which bread did you want? Enter a number: "))
    return Meat_list[Meat_selection-1]




#main program
print("Welcome to Sam's Sandwhich Shop")
bread_choice=bread_selection() 
print(f"Your selected bread: {bread_choice}")
meat_choice=Meat_selection()
print(f"your seletced Meat: {meat_choice}")
Cheese_choice=cheese_selection()
print(f"your seletced Cheese: {Cheese_choice}")
Dressing_choice=dressing_selection()
print(f"your seletced Dressing: {Dressing_choice}")


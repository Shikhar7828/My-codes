import random

def gamewin(comp, you ):
    if comp == you :
        return None

    elif comp == "gun":         
        if you == "snake":
            return False

        elif you == "Water":     
            return True

    elif comp == "water":
        if you == "snake":
            return True

        elif you == "Gun":
            return False

    elif comp == "snake":
         if you == "water":
            return False 

         elif you == "gun":
            return True
     


comp = ("comp Turn: snake(k) water(w) or gun(g) ?")
randNo = random.randint(1,3)
if randNo == 1:
    comp = "snake"
elif randNo == 2:
    comp = "water"
elif randNo == 3:
    comp = "gun"
else:
    None

you = input("your Turn: snake(k) water(w) or gun(g) ?")

print("you chose:- ",you )
print("computer choose:- ", comp)

a = gamewin(comp,you)
if a == None:
    print ("Tie")

elif a == True:
    print("you win ")

else:
     a == False
     print("you loose")






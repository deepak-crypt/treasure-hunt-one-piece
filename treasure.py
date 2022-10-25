print("Welcome To Treasure Hunt")
print("You have entered a mysterious place in search of a treasure called 'ONE PIECE'")
print(
    "You have the option to choose a 'DEVIL FRUIT' which will give you mysterious powers but in return you can't swim")
a = input(r"You want a devil fruit or not?(Yes/No)")
if a == "Yes":
    print("You got to eat a devil fruit called 'Gumo Gumo-No'")
    print("It gave you the power of elasticity and your body became rubber")
    df = True
else:
    print("You chose to have the ability to swim")
    df = False
print("On your Journey,You find a man hurting a woman")
b = input(r"Do you want to save her?(Yes/No)")
if b == "Yes":
    print("Looks like the man hurting the girl has elecric powers!!")
    c = input("Do you want to still save her(Yes/No)")
    if c == "Yes" and df:
        print(
            "Wooah!! He just tried to electrocute you, Thank God you ate Devil fruit and you became rubber. His attacks dont affect you and you defeated him!!!!")
        print("Looks like the girl you saved is a navigator!!")
        print(
            "The girl thanks you and asks 'Why are you here?' and you say that you are looking to find the 'ONE PIECE'")
        print("The girl says she has the map for it")
        print("YOU FOUND THE ONE PIECE!!!")
        print("Congragulations")
        print("Game over")
    else:
        print("SHIT! He zapped you and YOU DIED!")
        print("Game over")

else:
    print("Poor woman")
print("On your journey, You see a shipwreck in the ocean")
d = input("Do you want to scavange it?(Yes/No)")
if d == "Yes" and df == False:
    print("You found the map to ONE PIECE on the shipwreck")
    print("YOU FOUND THE ONE PIECE!!!")
    print("Congragulations")
    print("Game over")

elif d == "Yes" and df:
    print("You ate a devil fruit, YOU FOOL!!!, You can't swim")
    print("You drowned......")
    print("You Died")
    print("Game over")

else:
    print("Must be some pirate ship")
    print("You slipped some important oppirtunites and didn't find the ONE PIECE till your death........")
    print("Poor you")
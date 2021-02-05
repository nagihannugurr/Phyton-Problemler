devam=True
while devam:
    if devam==True:



        a=input("Pick rock, paper or scissors for player one: ")
        b=input("Pick rock, paper or scissors for player two: ")


        if ((a=="rock" and b=="scissors") or (a=="paper" and b=="rock") or (a=="scissors" and b=="paper")):
            print("Player one wins!")


        elif a.__contains__(b):
            print("Player one and two tied")

        else:
            print("Player two wins!")
    print("Do you want to play again? Y or N?")
    c = input()
    if c=="Y":
        devam=True
    else:
        print("Thanks for playing.")
        break










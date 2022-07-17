import random
#the person pick
person_choise=input("pleace pick rock , paper ,scissor :")

picks=['rock','paper','scissor']
#the computer with pick randmoly
computer_choise= random.choice(picks)

#the game statments
if person_choise == computer_choise:
        print('Draw')
elif person_choise=="rock" and computer_choise =="paper":
    print("computer win")
elif person_choise=="rock" and computer_choise =="scissor":
    print("you win")
elif person_choise=="paper" and computer_choise =="scissor":
    print('computer win')
elif person_choise=='paper' and computer_choise =="rock":
    print("you win")
elif person_choise=="scissor" and computer_choise =="rock":
    print("compputer win")
elif person_choise=="scissor" and computer_choise =="paper":
    print("you win")
#print the computer pick
print("the computer choise :" + computer_choise)
'''
the main module of the game
'''

from num_gen import Number
from ticket_gen import Ticket

print("LETS PLAY A GAME OF HOUSIE!!!!!!!!")
print("------------------------------------")
tick=0
while(1):
    print("1. Generate Ticket")
    print("2. Start Game")
    inp=input("Enter Input: ")
    if(inp.isalpha()):
        print("\nInvalid input. Enter 1 or 2.\n")
        continue
    inp=int(inp)
    if(inp!=1 and inp!=2):
        print("\nInvalid input. Enter 1 or 2.\n")
        continue
    if(tick==0 and inp==2):
        print("\nNot enough tickets. Generate more tickets.\n")
        continue
    if(tick==1 and inp==2):
        print("\nNot enough tickets. Generate more tickets.\n")
        continue
    if(tick>=2 and inp==2):
        print("\nGame begins!!!!!!!!!!\n")
        break
    if(inp==1):
        tic=Ticket()
        tc=tic.ticket_generator()
        for i in range(0,len(tc)):
            if(i%5==0):
                print("\n")
            print(str(tc[i]),end=" ")
        print("\n")
        tick+=1
flag=False
n=Number()
print("Press Q to quit game.")
print("Press any key to generate number.")
print("Game auto quits when all numbers are called.")
gen_num=n.get_generated_numbers()
while(len(gen_num)!=90):
    i=input()
    if(i=="Q" or i=="q"):
        print("\nGame ended abruptly.\n")
        flag=True
        break
    if(i=="c" or i=="C"):
        gen_num=n.get_generated_numbers()
        gen_num.sort()
        print("\n")
        print(gen_num)
        print("\n")
        continue
    num=n.num_generator()
    print("\nThe number is: " + str(num))
    print("\n")

if(flag==False):
    print("\nThe game ends.")
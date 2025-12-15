import random
import time 

def get_index():
    index = random.randint(1,52)
    while check_deck(index,deck):
        index = random.randint(1,52)
    return index

def check_deck(index,deck):
    if deck[index] == 1:
        return True
    return False

def index_card(index):
    if index > 13:
        if index % 13 == 0:
            number = 13
        else:    
            number = index % 13
    else:
        number = index
    return number

def get_a_card(card,player):
    if card>10:
        card = 10
    time.sleep(1)
    print(f"Player {player} your card value is {card}")
    if card == 1:
        time.sleep(0.5)
        card = int(input("Do you want the card to be 1 or 11 "))
        while card != 11 and card != 1:
            card = int(input("Do you want the card to be 1 or 11 "))
    return card

def house_get_a_card(card):
    if card>10:
        card = 10 
    if card == 1:
        card = 11
    time.sleep(1)
    return card

print("Great let's begin")

deck = [0] * 53 # used for simulating an actual deck 
#to make sure that a card can not be used more than 4 times (with the exeption of the VALUE 10 - as explained in the breakdown)
total = [0]*2 # two players
player = 1
for i in range(2):
        for x in range(2):
            index = get_index()
            deck[index] = 1
            number = index_card(index)
            card = get_a_card(number,player)
            total[i] = total[i] + card
        print(f"Your total is {total[i]}")
        player = player + 1
        while input("continue - - - "):
            print("")
#######################################################################################################---------------------->>>
# house draws one card at the start 
index = get_index()
deck[index] = 1
number = index_card(index)
house_first_card = house_get_a_card(number)
house_total = 0 
print("first house must draw one card ... ")
print(f"house first card is {house_first_card}")
house_total = house_first_card
###########################################################################################################------------------------>>>
player = 1 
winner = False
endgame = False
i = 0
stop = [0] * 2 
while  endgame == False:
    if stop[i] != 1:    
        state = int(input(f"player {player}, your card value is {total[i]}, do you want to hit ( 1 ) or fold ( 2 ) ? "))
        if state == 1:
            ## procedure to get a card ##
            index = get_index()
            deck[index] = 1
            number = index_card(index)
            card = get_a_card(number,player)
            ## procedure ends ##
            total[i] = total[i] + card
            print(f"Your total is {total[i]}")
            if total[i] > 21:
                print(f"Player {player} you are a loser!!! Careful not to be greedy, House wins :)")
                stop[i] = 1
        else:
            print(" you're no fun :( ")
            stop[i] = 1
        if total[i] == 21:
            print(f" WAIT A MINUTE ...    player {player} HAS 21 !!! YOU ARE THE WINNER. END THE GAME NOW")
            endgame = True
            twentyone = True
        if stop[0] == 1 and stop[1] == 1:
            print("Stop the game, let's see the results ... ")
            endgame = True
    if player == 1:
        i = 1
        player = 2
    else:
        i = 0 
        player = 1
###############################################################
# Finalise the results ####
if twentyone == False:    
    print("Now we must compare your cards to the house ... ")
    if total[0]>21:
        print(f"Player 1 your total is {total[0]}, therefore you lose !!! House takes the money")
        time.sleep(1)
    if total[1]>21:
        print(f"Player 2 your total is {total[1]}, therefore you lose !!! House takes the money")
        time.sleep(1)
    if total[0] <21 or total[1] < 21:
        for i in range(2):
            print(f"Player {i} you got {total[i]}")
            time.sleep(1)
        print(f"What did the house get. House first card was {house_total}")
        time.sleep(0.5)
        while house_total<17:
            index = get_index()
            deck[index] = 1
            number = index_card(index)
            house_total = house_total + house_get_a_card(number) 
            print(f"House's new total is {house_total}")
        for i in range(2):
            x = i + 1
            if total[i]>house_total and total[i] < 21:
                print(f"Player {x} wins!!!")
                time.sleep(0.5)
            else:
                print(f"Player {x} loses")

                time.sleep(0.5)

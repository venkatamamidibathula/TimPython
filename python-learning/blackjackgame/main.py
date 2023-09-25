# This project is for Blackjack game
import random
from turtle import clear


def dealcards():
    cards=[1,2,3,4,5,6,7,8,9,10,10,10,10,11]
    card=random.choice(cards)
    return card

def scorecalc(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    elif 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(userscore,computerscore):
    if userscore>21 and computerscore>21:
        return "You went over, computer wins"
    elif userscore == 0:
        return "User wins"
    elif computerscore == 0:
        return "Computer wins"
    elif userscore>21:
        return "You went over computer wins"
    elif computerscore>21:
        return "Computer went over user wins"
    elif userscore>computerscore:
        return "User score is higher, you win"
    elif userscore<computerscore:
        return "You loose....."
    else:
        return "You win......"

def playblackjack():

    print("\n ====================================================Welcome to Blackjack================================")
    user_cards=[]
    computer_cards=[]
    is_game_over=False
    for _ in range(2):
        user_cards.append(dealcards())
        computer_cards.append(dealcards())

    while not is_game_over:
        user_score=scorecalc(user_cards)
        computerscore=scorecalc(computer_cards)
        print(f"\n user cards are {user_cards} and userscore is {user_score} ")
        print(f"\n computer first care is {computer_cards[0]}")
        if user_score==0 or computerscore==0 or user_score>21:
            is_game_over=True
        else:
            user_deal=input("Please enter 'y' to choose another card or 'N' to not choose another card")
            if user_deal=="y":
                user_cards.append(dealcards())
            else:
                is_game_over=True
        while computerscore!=0 and computerscore<17:
                computer_cards.append(dealcards())
                computerscore=scorecalc(computer_cards)

    print(f"\n Your final hand score is {user_score} and your cards are {user_cards}")
    print(f"\n Computer score is {computerscore} and computer cards are {computer_cards}")
    print(f"\n {compare(user_score,computerscore)}")

while input("\n Do you want to play blackjack game 'y' for yes 'n' for no")=="y":
    clear
    playblackjack()
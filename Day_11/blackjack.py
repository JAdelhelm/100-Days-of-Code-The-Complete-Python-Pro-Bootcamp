import random
from art import logo
from replit import clear
# 11 ist Ass, was als eine 1 oder 11 gezählt werden kann


dealer = []
player  = []

def check_player_as(player_check_card_as):
    if (player_check_card_as == 11):
        if (player_check_card_as == 11) and ((sum(player) + player_check_card_as) <= 21): player.append(player_check_card_as)
        elif  (player_check_card_as == 11) and ((sum(player) + player_check_card_as) > 21): 
            player_check_card_as = 1;  player.append(player_check_card_as)
    else: player.append(player_check_card_as)

def dealer_append_card():
    if sum(dealer) <= 17: 
        dealer_check_card_as = random.choices(cards, k=1)[0]
        if (dealer_check_card_as == 11) and ((sum(dealer) + dealer_check_card_as) <= 21): dealer.append(dealer_check_card_as)
        elif  (dealer_check_card_as == 11) and ((sum(dealer) + dealer_check_card_as) > 21): 
            dealer_check_card_as = 1;  dealer.append(dealer_check_card_as)
        else: dealer.append(dealer_check_card_as)

if __name__ == '__main__':
    try:
        while True:
            cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
            start = input("Would you like to play a game of Blackjack? (y/n): ")
            clear()
                
            if start == 'y' or start == 'Y':
                print(logo)

                player = random.choices(cards, k=2)
                dealer = random.choices(cards, k=1)
                lose_dealer = False

                print(f"Your cards: {player}, current score: {sum(player)}")
                print(f"Dealer's cards: {dealer}, current score: {sum(dealer)}")
                print()

                while sum(player) <= 21:
                    print(f"Your cards: {player}, current score: {sum(player)}\n")

                    check_next_card = input("Type 'y' to get another card, type 'n' to pass: ")

                    if check_next_card == 'y' or check_next_card == 'Y':
                        # Check player as
                        player_card = random.choices(cards, k=1)[0]
                        print()
                        print("New card: " + str(player_card))
                        check_player_as(player_check_card_as=player_card)

                         # Check dealer as
                        dealer_append_card()

                    elif check_next_card == 'n' or check_next_card == 'N':
                        dealer_append_card()
                        if sum(dealer) > 21: lose_dealer = True

                        if sum(player) > sum(dealer) or lose_dealer == True:
                            print(f"Dealer cards: {dealer}, current score: {sum(dealer)}")
                            print(f"Your cards: {player}, current score: {sum(player)}")
                            print()
                            print("You win! :)\n")
                            print()
                            break
                        elif sum(player) < sum(dealer):
                            print(f"Dealer cards: {dealer}, current score: {sum(dealer)}")
                            print(f"Your cards: {player}, current score: {sum(player)}")
                            print()
                            print("You lose! :(\n")
                            print()
                            break
                        elif sum(player) == sum(dealer):
                            print(f"Dealer cards: {dealer}, current score: {sum(dealer)}")
                            print(f"Your cards: {player}, current score: {sum(player)}")
                            print()
                            print("Draw!")
                            print()
                            break
                else:
                    print()
                    print(f"Dealer cards: {dealer}, current score: {sum(dealer)}")
                    print(f"Your cards: {player}, current score: {sum(player)}")
                    print("You lose! :(")
                    print()
            else:
                break
    except:
        print("No valid input. Please try again.")

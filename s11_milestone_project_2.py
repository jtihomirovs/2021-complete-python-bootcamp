import random

import colorama
from colorama import Fore

colorama.init(autoreset=True)

# Global variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}


# Class Definitions

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.deck.append(created_card)

    def __str__(self):
        deck_composition = ''
        for card in self.deck:
            deck_composition += '\n' + card.__str__()
        return 'The deck has: ' + deck_composition

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Hand:
    def __init__(self):
        self.cards = []  # Card list in our hand
        self.value = 0  # Total value of hand
        self.aces = 0  # How many aces we have in our hand

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    # If a hand's value exceeds 21 but it contains an Ace, we can reduce the Ace's value from 11 to 1 and continue
    # playing.
    def adjust_for_ace(self):
        while self.value > 21 and self.aces > 1:
            self.value -= 10
            self.aces -= 1

    def __str__(self):
        return f'Player hand value: {self.value}'


class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet * 2

    def lose_bet(self):
        self.total -= self.bet

    def take_bet(self):
        while True:
            try:
                self.bet = int(input('Please enter your bet: '))
            except:
                print('Not valid bet value! Please try again!')
                continue
            else:
                if self.total - self.bet > 0:
                    print(f'Thank you, your bet is: {self.bet}')
                    break
                else:
                    print('Not enough chips!')

    def __str__(self):
        return f'Player chip amount: {self.total}'


# Functions

def show_some(player, dealer):
    print('Current Player cards:')
    for p_card in player.cards:
        print(p_card)
    print('Players hand sum:', player.value)

    print('Current Dealer cards:')
    for d_card in dealer.cards[:-1]:
        print(d_card)
        print('**Hidden card**')
    # Line below - for debug purposes
    # print('Dealers hand sum:', dealer.value)


def show_all(player, dealer):
    print('Current Player cards:')
    for p_card in player.cards:
        print(p_card)

    print('Current Dealer cards:')
    for d_card in dealer.cards:
        print(d_card)


def hit(deck, hand):
    hand.add_card(deck.deal())


def hit_or_stand(deck, hand):
    global player_turn  # to control an upcoming while loop
    while True:
        x = input("Would you like to Hit or Stand? Enter h or s: ")

        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print('Player stands. Dealer is playing!')
            player_turn = False
        else:
            print('Sorry, please try again')
            continue
        break


def replay():
    choice = ''

    while choice not in ['Y', 'N']:

        choice = input('Keep playing? (Y or N): ').upper()

        if choice not in ['Y', 'N']:
            print('Sorry, invalid choice!')

    if choice == 'Y':
        global player_turn
        player_turn = True
        return True
    else:
        return False


def player_busts(player, dealer, chips):
    print(Fore.RED + 'Player busted!')
    chips.lose_bet()
    print(chips)
    print(Fore.YELLOW + '*** Time to show all the cards! ***')
    show_all(player, dealer)


def player_wins(player, dealer, chips):
    print(Fore.GREEN + 'Player wins! Dealer loses!')
    chips.win_bet()
    print(chips)
    print(Fore.YELLOW + '*** Time to show all the cards! ***')
    show_all(player, dealer)


def dealer_busts(player, dealer, chips):
    print(Fore.GREEN + 'Dealer busted! Player wins!')
    chips.win_bet()
    print(chips)
    print(Fore.YELLOW + '*** Time to show all the cards! ***')
    show_all(player, dealer)


def dealer_wins(player, dealer, chips):
    print(Fore.RED + 'Dealer wins! Player loses!')
    chips.lose_bet()
    print(chips)
    print(Fore.YELLOW + '*** Time to show all the cards! ***')
    show_all(player, dealer)


def push():
    print(Fore.CYAN + 'Push! Dealer and player tie!')


# Main part - game logic
if __name__ == '__main__':
    game_on = True
    player_turn = True

    while game_on:
        print('Welcome to BlackJack! Get as close to 21 as you can without going over! \nDealer hits until she '
              'reaches 17. Aces count as 1 or 11.')

        # Create & shuffle the deck, deal two cards to each player
        deck = Deck()
        deck.shuffle()

        player_hand = Hand()
        dealer_hand = Hand()

        for i in range(2):
            player_hand.add_card(deck.deal())
            dealer_hand.add_card(deck.deal())

        # Set up the Player's chips
        player_chips = Chips()

        # Prompt the Player for their bet
        player_chips.take_bet()

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        while player_turn:
            hit_or_stand(deck, player_hand)
            show_some(player_hand, dealer_hand)

            if player_hand.value > 21:
                player_busts(player_hand, dealer_hand, player_chips)
                break

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        if player_hand.value <= 21:  # if player has not busted - otherwise game is over
            while dealer_hand.value < 17:
                hit(deck, dealer_hand)
            print(Fore.YELLOW + '*** Time to show all the cards!***')
            show_all(player_hand, dealer_hand)

            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)
            else:
                push()

        game_on = replay()

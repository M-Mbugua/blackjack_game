import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

#==========================================================================================

class Card:

    def __init__(self, suit, rank):

        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit

#==========================================================================================

class Deck:

    def __init__(self):

        self.deck = []

        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

    def __str__(self):
        deck_comp = ''

        for card in self.deck:
            deck_comp += "\n" + card.__str__()
        return "The deck has: " + deck_comp

#==========================================================================================

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # attribute to keep track of aces

    def add_card(self, card):
        # Card from Deck.deal() --> single card(suit,rank)
        self.cards.append(card)
        self.value += values[card.rank]

        # Track Aces
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):

        # IF TOTAL VALUE > 21 AND i STILL HAVE AN ACE
        # CHANGE MY ACE TO BE A 1 INSTEAD OF 11
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

#==========================================================================================

class Chips:

    def __init__(self):
        self.total = 100  # Can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

    # print(f"You have {} chips.\n")

#==========================================================================================

def take_bet(chips):

    while True:

        try:
            print(f"You have {chips.total} chips.")
            chips.bet = int(input("How many chips would you like to bet? "))
        except:
            print("Please provide an integer")
        else:
            if chips.bet > chips.total:
                print(f"Sorry, you do not have enough chips!")
            else:
                break


def hit(deck, hand):

    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop

    while True:
        x = input("\nHit or Stand. Enter h or s ")

        if x[0].lower() == 'h':
            hit(deck,hand)

        elif x[0].lower() == 's':
            print("Player stands, Dealer's turn")
            playing = False

        else:
            print("Sorry, I did not understand that. Please enter h or s only!")
            continue
        break

def show_some(player, dealer):

    # Show only one of the dealer's cards
    print("\nDealer's hand: ")
    print("Card Hidden! ")
    print(dealer.cards[1])

    # Show all (2 cards) of the player's hand
    print("\nPlayer's hand: ")
    for card in player.cards:
        print(card)

def show_all(player, dealer):

    # Show all the dealers cards
    print("\nDEALER'S HAND: ")
    for card in dealer.cards:
        print(card)

    # Calculate and display value
    print(f"\nValue of Dealer's hand is: {dealer.value}")

    # Show all the player's cards
    print("\nPLAYER'S HAND: ")
    for card in player.cards:
        print(card)
    # print("Player's cards are: ", *player.cards, sep = '\n')

    print(f"\nValue of Player's hand is: {player.value}")

#==========================================================================================

# END OF GAME SCENARIOS
def player_busts(player, dealer, chips):
    print("\nPLAYER BUSTS! DEALER WINS!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("\nPLAYER WINS!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("\nDEALER BUSTS! PLAYER WINS!")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("\nDEALER WINS!")
    chips.lose_bet()

def push(player, dealer):
    print("\nDealer and Player tie! PUSH!")

#==========================================================================================

# GAME LOGIC

playing = True

while True:
    # Print an opening statement
    print("\n***********************")
    print(" WELCOME TO BLACKJACK")
    print("***********************\n")

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up the Player's chips
    player_chips = Chips()

    # Prompt the Player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)

    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)

            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        hit(deck,dealer_hand)

        # Show all cards
        show_all(player_hand,dealer_hand)

        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)


    # Inform Player of their chips total
    print(f"\nPlayer's total chips are now {player_chips.total}")

    # Ask to play again
    new_game = input("Would you like to play another hand? y/n ")

    if new_game[0].lower() == 'y':
        playing = True
        continue

    else:
        print("Thank you for playing!")

        break

# BlackJack Game
import random

playing = False
chip_pool = 1000  # Total $ for player
bet = 1
restart_phrase = "Press 'd' to deal the cards again, or press 'q' to quit"

ranking = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
suits = ('H', 'D', 'C', 'S')
card_value = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10,
              'K': 10}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + self.suit

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self):
        print(str(self.rank + self.suit))


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.ace = False  # Because, Aces value also 11. So, We need to define

    def __str__(self):  # Print, current hand and list of hand
        hand_comp = ""

        for card in self.cards:
            card_name = card.__str__()
            hand_comp = " " + card_name

        return "The hand has %s" % hand_comp

    def card_add(self, card):  # Adding card to hand
        self.cards.append(card)

        if card.rank == 'A':  # Again, for Aces
            self.ace = True
        self.value = self.value + card_value[card.rank]

    def calculate_value(self):  # Calculate value of hand
        if self.ace is True and self.value < 12:
            return self.value + 10  # Aces 11, if they don't BUST the hand
        else:
            return self.value

    def draw(self, hidden):
        if hidden is True and playing is True:
            starting_card = 1
        else:
            starting_card = 0

        for x in range(starting_card, len(self.cards)):
            self.cards[x].draw()


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranking:
                self.deck.append(Card(self, rank))

    def shuffle(self):  # Shuffle the deck
        random.shuffle(self.deck)

    def deal(self):  # 1st item in the deck
        single_card = self.deck.pop()
        return single_card

    def __str__(self):
        deck_comp = ""  # Print, current hand and list of hand

        for card in self.cards:
            deck_comp = deck_comp + " " + deck_comp.__str__()

        return "The Deck has = " + deck_comp


def make_bet_amt():
    global bet
    bet = 0

    print("What amount of chips would you like to bet?")
    while bet == 0:
        while True:
            try:
                bet_comp = int(input("Please enter integer= "))

            except:
                print("It looks like, you did not enter an integer!")
                continue
            else:
                if bet_comp >= 1 and bet_comp <= chip_pool:
                    bet = bet_comp
                else:
                    print("Wrong input,or You have " + chip_pool + " ")
            break


def deal_cards():
    global result, chip_pool, bet, playing, deck, player_hand, dealer_hand

    deck = Deck()
    deck.shuffle()
    make_bet_amt()

    player_hand = Hand()
    dealer_hand = Hand()

    player_hand.card_add(deck.deal())
    player_hand.card_add(deck.deal())

    dealer_hand.card_add(deck.deal())
    dealer_hand.card_add(deck.deal())

    result = "Stand OR Hit? Press 's' or 'h' = "

    if playing is True:
        print("Fold, Sorry.")
        chip_pool = chip_pool - bet

    playing = True
    game_step()


def hit():
    global result, chip_pool, bet, playing, deck, player_hand, dealer_hand

    if playing:
        if player_hand.calculate_value() <= 21:
            player_hand.card_add(deck.deal())

        print("Player hand is %s" % player_hand)

        if player_hand.calculate_value() > 21:
            result = "BUSTED " + restart_phrase

            chip_pool = chip_pool - bet
            player_hand = False
    else:
        result = "Sorry, Can't HIT.. " + restart_phrase

    game_step()


def stand():
    global result, chip_pool, bet, playing, deck, player_hand, dealer_hand

    if playing is False:
        if player_hand.calculate_value() > 0:
            print("You can NOT stand. ")

    else:

        while dealer_hand.calculate_value() < 17:
            dealer_hand.card_add(deck.deal())

        if dealer_hand.calculate_value() > 21:
            result = "Dealer BUSTS .. You WINN!! " + restart_phrase
            chip_pool = chip_pool + bet
            playing = False

        elif dealer_hand.calculate_value() < player_hand.calculate_value():  # Better hand, PLAYER
            result = "You beat the dealer..!! You WINN " + restart_phrase
            chip_pool = chip_pool + bet
            playing = False

        elif dealer_hand.calculate_value() == player_hand.calculate_value():  # Tied,
            result = "Tied, PUSH!! " + restart_phrase
            playing = False

        else:  # Dealer, BEAT
            result = "Dealer WINN !" + restart_phrase
            chip_pool = chip_pool - bet
            playing = False
    game_step()


def game_step():
    print("")
    print("Player hand is= ")
    player_hand.draw(hidden=False)
    # Show player hand
    print("Player hand total is= " + str(player_hand.calculate_value()))

    print("Dealer hand is= ")
    dealer_hand.draw(hidden=True)  # Show dealer hand

    if playing is False:
        print("-- for a total of " + str(dealer_hand.calculate_value()))
        print("Chip Total= " + str(chip_pool))

    else:
        print(" with another card hidden upside down..")

    print(result)

    player_input()


def exit_game():
    print("GAME EXIT..")
    exit()


def player_input():
    enter_input = input().lower()

    if enter_input == 'h':
        hit()
    elif enter_input == 'd':
        deal_cards()
    elif enter_input == 's':
        stand()
    elif enter_input == 'e':
        exit_game()
    else:
        print("INVALID INPUT!!! Enter 'd' for deal-the-card \n 's' for stand \n 'h' for hit \n 'e' for EXIT ")
        player_input()


def start_game():
    info = '''WELCOME !!! to the Blackjack Game. Get as close to 21 as you can without going over!
    Dealer hits until he reaches 17. ACES as 1 or 11.
    Card output goes a letter followed by a number of face notation'''
    print(info)


deck = Deck()
deck.shuffle()

player_hand = Hand()
dealer_hand = Hand()

start_game()
deal_cards()

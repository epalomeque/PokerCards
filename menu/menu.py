# menu.py
import sys
from os import system, name
from deck.deck import Deck, CARD_VALUES, CARD_FIGURES


class Menu(object):
    ''' Print menu '''
    def __init__(self):
        self.deck = None
        self.choices = {
                "1": self.open_deck,
                "2": self.shuffle_deck,
                "3": self.serve_card,
                "4": self.count_cards,
                "5": self.print_cards,
                "6": self.quit
                }

    def display_menu(self):
        print("""
        Poker Deck Menu:
        1. Open new deck
        2. Shuffle deck
        3. Serve/Open card
        4. Count cards in deck
        5. Print Cards in deck
        6. Quit
        """)

    def run(self):
        '''Display the menu and respond to choices.'''
        while True:
            self.clear()
            self.display_menu()
            choice = input("\nEnter an option: ")
            action = self.choices.get(choice)
            if action:
                print("\n-----")
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def open_deck(self):
        self.deck = Deck(VALUES=CARD_VALUES, FIGURES=CARD_FIGURES)
        print("A new deck is open")
        self.deck.status()
        self.wait_pressed_key()

    def shuffle_deck(self):
        self.deck.shuffle()
        print("The deck is shuffled")
        self.wait_pressed_key()

    def serve_card(self):
        card = self.deck.serve_card()
        print("The served card is {0}".format(card.get_card()))
        self.wait_pressed_key()

    def count_cards(self):
        self.deck.status()
        self.wait_pressed_key()

    def print_cards(self):
        self.deck.print_deck()
        self.wait_pressed_key()

    # define our clear function
    def clear(self):

        # for windows
        if name == 'nt':
            _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    def wait_pressed_key(self):
        print("\n----------")
        input("Press 'Enter' key to continue")

    def quit(self):
        self.clear()
        print("\n----------")
        print("Thank you for using 'Poker Deck Menu'.")
        sys.exit(0)

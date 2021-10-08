# deck.py
import random

from cards.card import Card


CARD_VALUES = ("A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2")

CARD_FIGURES = {"D": "♦", "C": "♣", "H": "♥", "S": "♠"}


class Deck(object):

    def __init__(self, VALUES, FIGURES):
        self.cards = []

        for value in VALUES:
            for figure, char in FIGURES.items():
                card = Card(value=value, figure=char)
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def serve_card(self):
        return self.cards.pop()

    def status(self):
        print('There are {} cards in the deck.'.format(len(self.cards)))

    def print_deck(self):
        for count, value in enumerate(self.cards, start=1):
            print('{} - {} '.format(count, value.get_card()))
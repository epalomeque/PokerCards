# card.py

class Card(object):

    def __init__(self, value, figure):
        self.value = value
        self.figure = figure

    def get_card(self):
        return '[ {}{} ]'.format(self.value, self.figure)
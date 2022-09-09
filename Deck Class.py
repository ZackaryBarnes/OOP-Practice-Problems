

# Deck Class problem from ProgrammingExpert.io


import random

class Deck:
    suits = ["H", "D", "C", "S"]
    values = [str(i) for i in range(2, 11)] + ["J", "Q", "K", "A"]

    def __init__(self):
        self.cards = []
        self.create_deck()


    def create_deck(self):
        for suit in Deck.suits:
            for value in Deck.values:
                new_card = value + suit
                self.cards.append(new_card)
    

    def shuffle(self):
        random.shuffle(self.cards)

    
    def deal(self, n):
        dealt_cards = []

        for i in range(n):
            if len(self.cards) == 0:
                break

            deal_card = self.cards.pop()
            dealt_cards.append(deal_card)

        return dealt_cards


    def sort_by_suit(self):
        cards_by_suit = {"H": [], "D": [], "C": [], "S": []}

        for card in self.cards:
            card_suit = card[-1]
            cards_by_suit[card_suit].append(card)

        self.cards = (
            cards_by_suit["H"] +
            cards_by_suit["D"] +
            cards_by_suit["C"] +
            cards_by_suit["S"]
        )


    def contains(self, card):
        return card in self.cards

    def copy(self):
        copy = Deck()
        copy.cards = self.cards[:]
        return copy

    
    def get_cards(self):
        return self.cards[:]


    def __len__(self):
        return len(self.cards)


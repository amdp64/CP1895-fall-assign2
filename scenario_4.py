class Deck:
    def __init__(self):
        self.__deck = []
        
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "King", "Queen", "Ace"]
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

        for suit in suits:
            for rank in ranks:
                self.__deck.append(Card(suit, rank))

    def shuffle(self):
        import random
        random.shuffle(self.__deck)

    def deal(self):
        return self.__deck.pop()

    def count(self):
        return len(self.__deck)


class Card:
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank

    def getStr(self):
        return self.suit+" of "+self.rank


def main():
    print("Card Dealer")
    print("\nI have shuffled a deck of 52 cards.")
    deck = Deck()
    deck.shuffle()

    cards = int(input("\nHow many cards would you like?: "))
    print("\nHere are your cards:")
    for i in range(cards):
        card = deck.deal()
        print(card.getStr())

    print("\nThere are "+str(deck.count())+" cards left in the deck.")
    print("\nGood luck!")

if __name__ == "__main__":
    main()
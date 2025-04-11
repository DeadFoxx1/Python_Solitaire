from Class.Columns.Column import Column
from Class.Card import Card


class DrawDeck(Column):
    def __init__(
        self,
        num_of_cards: "int",
        deck: "list",
    ):
        super().__init__(num_of_cards, deck, False)
        self.contents.insert(0, Card(0, 0, True))

    def select_card(self, pos):
        for card in reversed(self.contents):
            if card.rect.collidepoint(pos):
                print("draw")
                return "draw"

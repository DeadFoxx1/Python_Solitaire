from Class.Columns.Column import Column
from Class.Card import Card


class PlayingColumn(Column):
    def __init__(
        self,
        num_of_cards: "int",
        deck: "list",
        can_accept_cards: "bool",
    ):
        super().__init__(num_of_cards, deck, can_accept_cards)
        self.contents.insert(0, Card(0, 14, True))

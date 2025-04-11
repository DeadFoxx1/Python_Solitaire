import pygame
import random
from setting import SCREEN_WIDTH, SCREEN_HEIGHT, SUITS
from Class.Columns.Column import Column
from Class.Rows.TopRow import TopRow
from Class.Rows.BottomRow import BottomRow
from Class.Card import Card

# create necessary pygame objects for screen and fps control
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

# create deck
# deck_main = Deck()

# create second deck with just foundation cards
# foundation = Deck(True)


def create_shuffled_deck():
    deck = [Card(suit, value, False) for value in range(1, 14) for suit in SUITS]
    random.shuffle(deck)
    return deck


# main deck
deck = create_shuffled_deck()

foundation_deck = [Card(suit, 0, True) for suit in SUITS]

bottom_row = BottomRow(deck, 7, foundation_deck)

top_row = TopRow(deck, 7)

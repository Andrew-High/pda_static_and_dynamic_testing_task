import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame (unittest.TestCase):
    def setUp(self):
        self.card_1 = Card("Spades", 1)
        self.card_2 = Card("Diamonds", 7)
        self.card_game = CardGame(self.card_1, self.card_2)
        self.cards = [self.card_1, self.card_2]

    def test_check_for_ace(self):
        self.assertEqual(True, self.card_game.check_for_ace(self.card_game.card1))

    def test_highest_card(self):
        result = self.card_game.highest_card(self.card_1, self.card_2)
        self.assertEqual(7, result)

    def test_cards_total(self):
        result = self.card_game.cards_total(self.cards)
        self.assertEqual("You have a total of 8", result)
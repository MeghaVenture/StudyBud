# cards.py
# classes and functions related to flashcards

# IMPORTS
from abc import ABCMeta, abstractmethod
from statistics import mean, median

#CLASSES
class Card():
    """the basic card for any topic"""
    def __init__(self, deck=str, word=str, definitions={}):
        self.deck = deck
        self.word = word
        self.definitions = definitions
        history = [] #list ordered by entry time (newest=last)
        rank = 0
        audio = {} #dict to allow gendered/accent/form varity
        ipa = {} #dict to allow mutliple standard pronouniation
    #ADD/CHANGE by code
    def find_ipa(self):
        """scrapes ipa from web and saves to dict"""
        pass
    def find_audio(self):
        """scrapes audio from web and saves to dict"""
        pass
    def update_rank(self):
        """calculates the play data stored in the history list - to be used to change the rank"""
        last_score = history[-1]
        last_three_avg = (int(history[-1])+int(history[-2])+int(history[-3]))/3
        play_median = median(history)
        play_mean = mean(history)
        total_play = (play_mean + play_median)/2
        recent_play = (last_score + last_three_avg)/2
        recent_play_weight = 50
        total_play_weight = 10
        rank = ((((total_play * total_play_weight)+(recent_play * recent_play_weight))/2)+rank)/2
        return rank
    #ADD by user
    def add_tag(self, tag):
        """adds a tag to itself/card"""
        pass
    def add_audio(self, tag):
        """adds an audio file to the list "audio" in itself/card"""
        pass
    #DELETE
    def delete_card(self):
        """removes itself/card"""
        pass

class Card_Factory():
    @staticmethod
    def create_card(card_type, deck, word, definition):
        pass
    @staticmethod
    def import_cards(card_type, deck, file):
        pass
    @staticmethod
    def batch_create_cards(card_type, deck, file):
        pass

class Language_Card(Card):
    def __init__(self):
        Card.__init__()
        translations = {}
        forms = {}
        synonyms = []
        antonyms = []
        articles = {}
        tenses = {}
        parts_of_speech = []




# cards.py
# classes and functions related to flashcards

# IMPORTS
from abc import ABCMeta, abstractmethod
from statistics import mean, median

# VARIABLES
DECK_NAMES = []
TAG_LIST = []
CARD_RANKS = {}

#CLASSES
class Card():
    """the basic card for any topic"""
    def __init__(self, deck=str, side_a=str, side_b=dict, wrong_a=[], wrong_b=[], history=[], rank=0, audio={}, tags=[]):
        # deck, side_a & side_b are required but others are optional
        self.deck = deck
        self.side_a = side_a
        self.side_b = side_b
        self.wrong_a = wrong_a # user entered wrong answers (or misspellings) etc
        self.wrong_b = wrong_b # user entered wrong answers/definitions
        self.history = history
        self.rank = rank
        self.audio = audio
        self.tags = tags

    # By code
    def rec_history(self):
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

    # By user
    ## Deck and Card
    def rename_deck():
        '''renames the deck value for a card'''
        pass

    def del_deck(self):
        """deletes the deck with option to also delete cards inside"""
        pass

    def del_card(self):
        """deletes the card"""
        pass

    ## Parts of a Card
    ### Side A
    def edit_side_a(self):      # the "word"
        """edits the side_a value for the card"""
        pass

    ### Side B
    def add_side_b(self):       # the "definitions
        """adds another side_b value to a card"""
        pass

    def edit_side_b(self):
        """"edits a side_b value of a card"""
        pass

    def del_side_b(self):
        """deletes a side_b value from a card"""
        pass

    ### Wrong A
    def add_wrong_a(self):
        """adds a "wrong_a" answer to the card"""
        pass

    def edit_wrong_a(self):
        """edits a "wrong_a" value on the card"""
        pass

    def del_wrong_a(self):
        """deletes a "wrong_a" value on the card"""
        pass

    ### Wrong B
    def add_wrong_b(self):
        """adds a "wrong_b" answer to the card"""
        pass

    def edit_wrong_b(self):
        """edits a "wrong_b" value on the card"""
        pass

    def del_wrong_b(self):
        """deletes a "wrong_b" value on the card"""
        pass

    ### Tags
    def add_tag(self, tag):
        """adds a tag to itself/card"""
        pass

    def edit_tag(self, tag):
        """edits a tag to itself/card"""
        pass

    def del_tag(self, tag):
        """deletes a tag to itself/card"""
        pass

    ### Audio
    def add_audio(self, tag):
        """adds an audio file to the list "audio" in itself/card"""
        pass

    def edit_audio(self, tag):
        """edits an audio file to the list "audio" in itself/card"""
        pass

    def del_audio(self, tag):
        """deletes an audio file to the list "audio" in itself/card"""
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
    """the card tailored for language learning"""
    def __init__(self, deck=str, side_a=str, side_b=dict, wrong_a=[],
                 wrong_b=[], history=[], rank=0, audio={}, tags=[], ipa={},
                 forms={}, articles={}, tenses={}, parts_of_speech=[]):
        Card.__init__()
        self.deck = deck
        self.side_a = side_a  # word
        self.side_b = side_b  # definitions
        self.wrong_a = wrong_a
        self.wrong_b = wrong_b
        self.history = history
        self.rank = rank
        self.audio = audio
        self.tags = tags
        self.ipa = ipa
        self.forms = forms
        self.articles = articles
        self.tenses = tenses
        self.parts_of_speech = parts_of_speech
        #self.synonyms = []
        #self.antonyms = []
        #self.translations = {}

    # INHERITED
    ## By Code
    #def rec_history(self):
    #def update_rank(self):
    ## By User
    ### Deck and Card
    #def rename_deck():
    #def del_deck(self):
    #def del_card(self):
    ### Parts of a Card
    #### Side A
    #def edit_side_a(self):         # the "word"
    #### Side B
    #def add_side_b(self):          # the "definitions
    #def edit_side_b(self):
    #def del_side_b(self):
    #### Wrong A
    #def add_wrong_a(self):
    #def edit_wrong_a(self):
    #def del_wrong_a(self):
    #### Wrong B
    #def add_wrong_b(self):
    #def edit_wrong_b(self):
    #def del_wrong_b(self):
    #### Tags
    #def add_tag(self, tag):
    #def edit_tag(self, tag):
    #def del_tag(self, tag):
    #### Audio
    #def add_audio(self, tag):
    #def edit_audio(self, tag):
    #def del_audio(self, tag):

    # IPA
    def add_ipa(self):
        """adds an "ipa" value to the card"""
        pass
    def edit_ipa(self):
        """edits an "ipa" value on the card"""
        pass
    def del_ipa(self):
        """deletes an "ipa" value on the card"""
        pass
    # Forms
    def add_form(self):
        """adds a "form" value to the card"""
        pass
    def edit_form(self):
        """edits a "form" value on the card"""
        pass
    def del_form(self):
        """deletes a "form" value on the card"""
        pass
    # Articles
    def add_article(self):
        """adds an "article" value to the card"""
        pass
    def edit_article(self):
        """edits an "article" value on the card"""
        pass
    def del_article(self):
        """deletes an "article" value on the card"""
        pass
    # Tenses
    def add_tense(self):
        """adds a "tense" value to the card"""
        pass
    def edit_tense(self):
        """edits a "tense" value on the card"""
        pass
    def del_tense(self):
        """deletes a "tense" value on the card"""
        pass
    # Part Of Speech
    def add_part_of_speech(self):
        """adds a "part of speech" value to the card"""
        pass
    def edit_part_of_speech(self):
        """edits a "part of speech" value on the card"""
        pass
    def del_part_of_speech(self):
        """deletes a "part of speech" value on the card"""
        pass

# FUNCTIONS

def make_wrong_a():
    # Spellings
    ## remove or add spaces or - from compound words ("backpack" > "back pack" or "back-pack")
    ## Capitalized or not
    ## wrong article infront ("dogs" > "a dogs" | "apple" > "a apple")
    ## add/remove double letters ("letter" > "leter" | "movie" > "moovie" or "movvie")
    ## switch letters
        ## switch in place ("Letter" > "Lettre")
        ## switch letters with simular ("Cow" > "Kow" or "Caw"/"Cuw" or "Coe"/"Cou"

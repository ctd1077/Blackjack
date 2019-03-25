#!/usr/bin/env python3
# BlackJack Game
# By: Cambron Deatherage

import pandas as pd
import random

lst = []
hand = []

class Player():
    '''Parent Class Player'''

    def __init__(self):

        self.score = 0

    def hand(self):

        return hand[0]


class HumanPlayer(Player):
    '''Child Class HumanPlayer'''
    def hand(self):
        return None

class Computer(Player):
    '''Child Class ComputerPlayer'''
    def hand(self):

        #while throw != 'rock'and throw != 'paper'and throw != 'scissors':
            #print('Sorry try again')
            #throw = input('rock, paper, scissors? >')
        #return (throw)
        return None

class Game():
    def __init__(self):
        self.p1 = HumanPlayer()
        self.p2 = ComputerPlayer()

    def new_deck():
        '''A fucntion to create a new deck of cards'''
        cards = pd.Series(['2','3','4','5','6','7','8','9','10','J','Q',\
        'K','A'])
        Diamonds = pd.Series(cards)
        Clubs = pd.Series(cards)
        Spades = pd.Series(cards)
        Hearts = pd.Series(cards)
        deck = pd.concat({'Hearts':Hearts,'Spades':Spades,'Clubs':Clubs,\
        'Diamonds':Diamonds}, axis=1)
        return deck

    def deal_Card(df, lst):
        ''' This function deals a card, one card at a time
        and keeps track of cards played in a deck
        With out all the Debugging print statements'''
        played = False
        while played is False:
            select_suit = random.choice(suit)
            card = random.choice(cards)
            tup = (select_suit, card)
            if tup in lst:
                played = False
                if len(lst) > 51:
                    played = True
                    print('Deck is empty')
                    break
                continue
            else:
                lst.append((select_suit,card))
                deck.loc[deck[select_suit] == card, select_suit] = None
                played = True
                break
        return select_suit, card

    def points(card):
        ''' This function decides if the card varible can be dtype of int
        if so then the point value is the value of the card
        if it is a str then it's a face card
        if Ace then 11 points else all other face cards are 10 points'''
        try:
            card = int(card)
            point = int(card)
            print('This card is an int:')
            print(card)
        except:
            card = str(card)
            print('This card is a str:')
            print(card)
            if card == 'A':
                point = 11
                print('This card is an Ace')
                print(point)
            else:
                point = 10
                print(point)
        return point

    def play_game(self):
        pass

if __name__ == '__main__':
    answer = input('Welcome to Blackjack!\n Would you like to play a game?\n\
    Enter [Y]es or [N]o:')
# answer is a player class list
# p2 is output input from the user

    while answer != 'N':
        print('Great and good luck!\nGames last for 3 rounds')
        Game = Game()
        answer = input('Would you like to play another game:')
        break

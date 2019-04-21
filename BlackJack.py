#!/usr/bin/env python3
# BlackJack Game
# By: Cambron Deatherage

import pandas as pd
import random
import time


suit = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
cards = pd.Series(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q',
                  'K', 'A'])


class Player():
    '''Parent Class Player'''
    def __init__(self):

        self.score = 0


class HumanPlayer(Player):
    '''Child Class HumanPlayer'''
    def __init__(self):
        Player.__init__(self)

    def deal(self, lst):
        deal = deal_Card(lst)
        return deal

    def point(self, card):
        point = points(card)
        self.score += point
        return point


class Dealer(Player):
    '''Child Class ComputerPlayer'''
    def __init__(self):
        Player.__init__(self)

    def deal(self, lst):
        deal = deal_Card(lst)
        return deal

    def point(self, card):
        point = points(card)
        self.score += point
        return point


def new_deck():
        '''A fucntion to create a new deck of cards'''
        # deck = pd.concat({'Hearts':Hearts,'Spades':Spades,'Clubs':Clubs,
        # 'Diamonds':Diamonds}, axis=1)
        lst = []
        return lst


def deal_Card(lst):
    ''' This function deals a card, one card at a time
    and keeps track of cards played in a deck
    With out all the Debugging print statements'''
    global card
    played = False
    while played is False:
        card = random.choice(cards)
        select_suit = random.choice(suit)
        tup = (select_suit, card)
        if tup in lst:
            played = False
            if len(lst) > 51:
                played = True
                print('Deck is empty')
                break
            continue
        else:
            lst.append((select_suit, card))
            played = True
            break
    return card, select_suit


def points(card):
    ''' This function decides if the card varible can be dtype of int
    if so then the point value is the value of the card
    if it is a str then it's a face card
    if Ace then 11 points else all other face cards are 10 points'''
    try:
        card = int(card)
        point = int(card)
    except:
        card = str(card)
        if card == 'A':
            point = 11
        else:
            point = 10
    return point


class Game():

    def __init__(self):
        self.p1 = HumanPlayer()
        self.p2 = Dealer()
        self.player_cards = []
        self.dealer_cards = []

    def start_Game(self):

        p1 = self.p1.deal(lst)
        self.player_cards.append(p1)
        self.p1.point(card)
        time.sleep(2)
        print('Player gets the first card: ', self.player_cards)
        p2 = self.p2.deal(lst)
        self.dealer_cards.append(p2)
        self.p2.point(card)
        time.sleep(2)
        print('Dealer gets first card face down ')
        p1 = self.p1.deal(lst)
        self.player_cards.append(p1)
        self.p1.point(card)
        time.sleep(2)
        print('Player gets the second card: ', p1)
        p2 = self.p2.deal(lst)
        self.dealer_cards.append(p2)
        self.p2.point(card)
        time.sleep(2)
        print('Dealer gets second card: ', self.dealer_cards[1])
        win = False
        if self.p1.score == 22:
            print('Two aces will be played as a soft hand:')
            self.p1.score == 12
        elif self.p1.score == 21:
            print('BlackJack!')
            print('Congradulations you win!')
            win = True
        time.sleep(2)
        print('Your hand is : ', self.player_cards, 'for a total of ',
              self.p1.score, 'points')
        time.sleep(1)
        print('The only card the Dealer shows is :', self.dealer_cards[1])
        return win

    def player_Round(self):
        while self.p1.score <= 21:
            time.sleep(1)
            ans = input('Would you like another card? [Y]es or [N]o? ')
            win = False
            if ans == 'y':
                p1 = self.p1.deal(lst)
                self.p1.point(card)
                self.player_cards.append(p1)
                if self.p1.score <= 21:
                    print('Your card is: ', p1,)
                    print('Hand: ', self.player_cards, 'Total points',
                          self.p1.score)
                    win = False
                    continue
                elif self.p1.score > 21:
                    print('Your card is: ', p1)
                    time.sleep(2)
                    print('Sorry you bust and dealer wins')
                    win = True
                    break
            else:
                break
        return win

    def dealer_Round(self):
        print('Dealer shows his cards: ', self.dealer_cards)
        game = True
        if self.p2.score == 22:
            time.sleep(2)
            print('Two aces will be played as a soft hand for 12 points:')
            self.p2.score == 12
        elif self.p2.score == 21:
            print('21! Dealer wins!')
            game = False
            win = True
        while game is True:
            if self.p2.score <= 16:
                print('Dealer takes another card: ')
                p2 = self.p2.deal(lst)
                self.dealer_cards.append(p2)
                self.p2.point(card)
                time.sleep(2)
                print('Dealers card is: ', p2)
                game = True
                win = False
                continue
            elif self.p2.score == 21:
                time.sleep(2)
                print('Dealer has 21 points')
                print('Sorry you lose!')
                game = False
                win = True
                break
            # Try using just a else statement and see what happens
            elif self.p2.score > 21:
                time.sleep(2)
                print('Dealer has bust!')
                print('You Win!')
                game = False
                win = True
                break
            else:
                time.sleep(2)
                print('Dealer stays with ', self.p2.score, ' points')
                win = False
                break
        return win

    def wl(self):
        if self.p1.score <= self.p2.score:
            print('You Lose!')
        else:
            print('You Win!')


if __name__ == '__main__':
    answer = input('Welcome to Blackjack!\n Would you like to play a game?\n\
    Enter [Y]es or [N]o:')
    answer = answer.upper()

    while answer != 'N':
        print('Good luck!\n')
        lst = new_deck()
        print('Dealer shuffles the deck\n')
        game = Game()
        game.start_Game()
        win = game.player_Round()
        if win is False:
            win = game.dealer_Round()
            if win is True:
                print('Game Over!')
            else:
                game.wl()
        else:
            print('Game Over!')

        answer = input('Would you like to play another game:')
        answer = answer.upper()
        if answer is 'N':
            break
    print('Thank you and have a great day.')

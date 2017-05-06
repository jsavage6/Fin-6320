# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 11:43:52 2017

@author: Joshua
"""
#import random

#print("Lets play a game of hangman, here we go")

#count = 0

#class Hangman():
    
 #   words = ("wanker", "retard", "idiot", "homework", "school", "hangman")
  #  guesses = 0
   # letters_used = ""
    #secretword = random.choice(words)
    
   # while guesses < 6:
    #    guess = input("Guess a letter")
        
     #   if guess in words and not letters_used:
      #      print("good guess")
       #     letters_used += "," + guess
        #    print("letters used: ", letters_used)
            
       # elif guess not in words and not(letters_used):
        #    guesses += 1
         #   print('Wrong, you have', 6 - guesses, " guesses left")
            
      #  else:
       #     print("your dumb, try again")
    
import random

name = str(input("What's your name?"))
print("Hello,", name + "!")
failures = 0
allowed = 1
guessed = str()
wordlist = ['hangman', 'dinner', 'computer', 'america', 'olympics', 'football', 'minecraft', 'jacket', 'cabbage', 'electricity', 'dog',
            'pasta', 'japan', 'water', 'programming', 'anaconda', 'onehunga', 'name', 'windows', 'curtains', 'bieber', 'kirito',
            'montenegro', 'wheel', 'civilization', 'physics', 'bluebird' 'table', 'ACDC', 'guardian yam' 'mario', 'parachute', 'agario', 'obama',
            'youtube', 'putin', 'dairy', 'christianity', 'club penguin', 'oskahlavistah', 'coins', 'agitating', 'jumping', 'eating',
            'your mom', 'executive', 'car', 'jade', 'abraham', 'sand', 'silver', 'uranium', 'oscar is gay', 'bioshock', 'fizzle', 'moonman', 'watermelon',
            'WAHAHAHAHAHA', 'steve jobs', 'extreme', 'weeaboo jones', 'hot damn', name]

def correct(guess):
    if guess in word:
        if guess not in guessed:
            print("Correct")
            return(True)
    else:
        if guess not in word and len(guess) == 1 and guess in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ':
            if guess not in guessed:
                print("Incorrect!")
                return(False)

print("Guess this word!")
print("You can input any letter from A to Z and the space key.")
wordnumber = random.randint(0, len(wordlist))
word = (wordlist[wordnumber])
print("_ "*len(word))
while failures < allowed:
    guess = str(input("Guess a letter!"))
    if len(guess) != 1 or guess not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ':
        print("That is not a letter, try again.")
    if guess in guessed:
        print("You have already guessed that letter, try again.")
    iscorrect = correct(guess)
    guessed = guessed, guess
    if iscorrect == True:
        print("Word display still in development")
    if iscorrect == False:
        print("You suck")
        failures = failures+1
        print("You have", allowed , "guesses left.")
    if failures == allowed:
        replay = str(input("Press 1 to play again, press 2 to exit."))
        if replay == 1:
            break
        else:
            quit()


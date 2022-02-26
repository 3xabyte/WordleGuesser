"""
--------------------------------------------------------
Title:      Wordle Guesser
File Name:  Guesser.py
Author:     Matt McBurnie
Version:    1.0.0
Date:       February 26, 2022
--------------------------------------------------------
"""

from copy import deepcopy
from Characters import Letters
from Counts import LetterCount

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

class Guesser:

    def __init__(self):
        """
        --------------------------------------------------------
        Initializes the Guesser object
        Use: g = Guesser()
        --------------------------------------------------------
        Parameters:
            None
        Returns:
            A new Guesser object (Guesser)
        --------------------------------------------------------
        """
        f = open("words.txt", "r")

        self._possible_chars = []
        temp = []

        for x in ALPHABET:
            temp.append(x)

        for x in range(5):
            self._possible_chars.append(deepcopy(temp))

        self._remaining_letters = Letters()
        self._yellows = []
        self._words = f.read().split(",")
        self._words.sort()
        self._print_words(True)

        f.close()
        return

    def _search(self, guess):
        """
        --------------------------------------------------------
        Goes through each word and the word gets removed if the
        requirements are not met. 
        Use: self._search(guess)
        --------------------------------------------------------
        Parameters:
            guess - The user's guess is a five letter word (str)
        Returns:
            None
        --------------------------------------------------------
        """

        green_chars = ""
        yellow_chars = ""
        
        # User inputs for green and yellow characters. The loops only break if the user's input is valid.
        while(True):
            valid = False
            green_chars = input("Please type your guess again, but replace gray and yellow characters with '-': ")

            if(len(green_chars) == 5):
                for i in range(5):
                    if(green_chars[i] != guess[i] and green_chars[i] != '-'):
                        break
                    elif(i == 4):
                        valid = True

            if(valid):
                break

            print("Invalid input, please try again.")

        while(True):
            valid = False
            yellow_chars = input("Please type your guess again, but replace gray and green characters with '-': ")

            if(len(yellow_chars) == 5):
                for i in range(5):
                    if(yellow_chars[i] != guess[i] and yellow_chars[i] != '-'):
                        break
                    elif(i == 4):
                        valid = True

            if(valid):
                break

            print("Invalid input, please try again.")

        guess = guess.lower()
        green_chars = green_chars.lower()
        yellow_chars = yellow_chars.lower()   

        self._search_greens(green_chars)
        self._search_yellows(yellow_chars)
        self._search_grays(guess, green_chars, yellow_chars)
        self._update_counts(guess, green_chars, yellow_chars)


        i = 0
        length = len(self._words)

        while(i < length):
            popped = False
            # Anything that is not in the possible characters
            for x in range(5):
                if(self._words[i][x] not in self._possible_chars[x]):
                    popped = True
                    self._words.pop(i)
                    length -= 1
                    break
            
            if(not popped):
                # Anything that is above the max or below the min
                counts = LetterCount()
                counts.add_word(self._words[i])
                letter_count = counts.get_letters()

                for char in letter_count:

                    curr_char_count = counts.get_count(char.char())
                    minimum = self._remaining_letters.get_min(char.char())
                    maximum = self._remaining_letters.get_max(char.char())

                    if((curr_char_count > maximum) or (curr_char_count < minimum)):
                        popped = True
                        self._words.pop(i)
                        length -= 1
                        break

            if(not popped):
                i += 1

    
    def _search_greens(self, greens):
        """
        --------------------------------------------------------
        Goes through [greens]. Set self._possible_chars where
        the green characters are to only the green character at
        that index.
        Use: self._search_greens(greens)
        --------------------------------------------------------
        Parameters:
            greens - A 5 character string (str)
        Returns:
            None
        --------------------------------------------------------
        """

        # Check the green characters
        for i, g_char in enumerate(greens):
            if(g_char.isalpha()):
                self._possible_chars[i] = [g_char]



    
    def _search_yellows(self, yellows):
        """
        --------------------------------------------------------
        Goes through [yellows]. Remove letters from
        self._possible_chars where the yellow characters are.
        Use: 
        --------------------------------------------------------
        Parameters:
            yellows - A 5 character string (str)
        Returns:
            None
        --------------------------------------------------------
        """

        self._yellows = []

        # Check the yellow characters
        for i, y_char in enumerate(yellows):
            if(y_char.isalpha()):
                self._yellows.append(y_char)
                
                temp = self._possible_chars[i]
                self._possible_chars[i] = []

                for x in ALPHABET:
                    if(x != y_char and x in temp):
                        self._possible_chars[i].append(x)

            


    def _search_grays(self, guess, greens, yellows):
        """
        --------------------------------------------------------
        Removes all characters that are not in greens or
        yellows. Also removes gray characters that exist in 
        greens.
        Use: self._search_grays(guess, greens, yellows)
        --------------------------------------------------------
        Parameters:
            guess - The user's guess (str)
            greens - A 5 character string with confirmed
                     characters (str)
            yellows - A 5 character string where characters
                      exist in the actual word (str)
        Returns:
            None
        --------------------------------------------------------
        """

        grays = ""

        for i, char in enumerate(guess):
            if((char == greens[i]) or (char == yellows[i])):
                grays += '-'
            else:
                grays += char

        for i, char in enumerate(grays):

            if(char != '-'):
                for y in range(5):

                    """
                    The following needs to be satisfied to be popped from the possible character list:
                    - The character exists in the list
                    - The length of the list does not equal 1
                    """
                    if(char in self._possible_chars[y] and len(self._possible_chars[y]) != 1):

                        if(char not in greens and char not in yellows):
                            self._possible_chars[y].pop(self._possible_chars[y].index(char))
                        elif(char != greens[y] and char in greens and char not in yellows):
                            self._possible_chars[y].pop(self._possible_chars[y].index(char))
                
                if(char in yellows):
                    self._possible_chars[i].pop(self._possible_chars[i].index(char))

    def _update_counts(self, guess, greens, yellows):
        """
        --------------------------------------------------------
        Updates the min and max counts of each letter.
        Use: self._update_counts(guess, greens, yellows)
        --------------------------------------------------------
        Parameters:
            guess - The user's guess (str)
            greens - A 5 character string with confirmed
                     characters (str)
            yellows - A 5 character string where characters
                      exist in the actual word (str)
        Returns:
            None
        --------------------------------------------------------
        """

        grays = ""
        num_of_grays = 0
        inside_words = ""           # Greens and yellows together
        counts = LetterCount()
        yellow_count = LetterCount()

        for i, char in enumerate(guess):
            if((char == greens[i]) or (char == yellows[i])):
                grays += '-'
            else:
                grays += char
                num_of_grays += 1

        for g_char in greens:
            if(g_char.isalpha()):
                inside_words += g_char

        for y_char in yellows:
            if(y_char.isalpha()):
                inside_words += y_char
                yellow_count.add(y_char)

        counts.add_word(inside_words)

        for i, char in enumerate(ALPHABET):

            # Characters not in the guess will have a max of [num_of_grays] possible characters
            if(char not in guess):
                if(self._remaining_letters.get_max(char) > 0):
                    self._remaining_letters.set_max_letter(char, num_of_grays)
            else:
                # The purely gray characters will be set to 0
                if(char not in greens and char not in yellows):
                    self._remaining_letters.set_max_letter(char, 0)
                else:
                    # Adjust min amount of characters
                    if(self._remaining_letters.get_min(char) < counts.get_count(char)):
                        self._remaining_letters.set_min_letter(char, counts.get_count(char))

                    # Adjust max amount of characters to amount inside the word.
                    if(char in inside_words and char in grays):
                        self._remaining_letters.set_max_letter(char, counts.get_count(char))
                    else:
                        self._remaining_letters.set_max_letter(char, 5 - counts.get_count_except(char))

                    if(char in yellows and char in greens and char not in grays):
                        self._remaining_letters.set_max_letter(char, 5 - yellow_count.get_count(char))
                    elif(char in yellows and char not in greens and char not in grays):
                        self._remaining_letters.set_max_letter(char, 5 - counts.get_count(char))
                    elif(char in yellows and char not in greens and char in grays):
                        self._remaining_letters.set_max_letter(char, counts.get_count(char))
                      
    def _print_words(self, write_to_file):
        """
        --------------------------------------------------------
        Writes all the possible words to a .txt file along
        with the amount of words.
        Use: self._print_words(write_to_file)
        Use: print(self._print_words(write_to_file))
        --------------------------------------------------------
        Parameters:
            write_to_file - If True, write the possible words to
                            a .txt file. If false, just return
                            the output (boolean)
        Returns:
            All possible remaining words (str)
        --------------------------------------------------------
        """
        output = "{:} Possible Words\n".format(len(self._words))
        output += ("=" * 152) + "\n"

        for i, word in enumerate(self._words):
            output += word + "  "
            if((i + 1) % 22 == 0):
                output += "\n"
        
        if(write_to_file):
            f = open("possible_words.txt", "w")
            f.write(output)
            f.close()

        return output

    def _print_possibilities(self):
        """
        --------------------------------------------------------
        Prints all the possible characters at each position
        Use: self._print_possibilities()
        --------------------------------------------------------
        Parameters:
            None
        Returns:
            None
        --------------------------------------------------------
        """
        for i, x in enumerate(self._possible_chars):
            possibilities = ""
            for y in x:
                possibilities += y
            print("Character {:}: {:}".format(i + 1, possibilities))

    def play(self):
        """
        --------------------------------------------------------
        The main function. Allows the user to guess words and
        get possible words.
        Use: g.play()
        --------------------------------------------------------
        Parameters:
            None
        Returns:
            None
        --------------------------------------------------------
        """

        guesses = 6

        while(guesses > 0):
            print("=================================================")
            print("{:} guesses remaining".format(guesses))      
            user = input("Functions:\nS: Stops the game\nP: Prints the possible words\nR: Restarts the game\nC: All possible characters\nPlease enter a word: ")

            if(user == "S"):
                break
            elif(user == "P"):
                print()
                print(self._print_words(False))
                print()
            elif(user == "R"):
                self.__init__()
                guesses = 6
            elif(user == "C"):
                self._print_possibilities()
            else:
                user = user.lower()
                if(len(user) > 5):
                    print("Word is too long, please try again.")
                elif(len(user) < 5):
                    print("Word is too short, please try again")
                elif(user not in self._words):
                    print("Word not available, please try again.")
                else:
                    guesses -= 1
                    self._search(user)
                    self._print_words(True)
            
            print("=================================================")

            
game = Guesser()
game.play()

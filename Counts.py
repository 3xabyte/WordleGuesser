"""
--------------------------------------------------------
Title:      Wordle Guesser
File Name:  Counts.py
Author:     Matt McBurnie
Version:    1.0.0
Date:       February 26, 2022
--------------------------------------------------------
"""

from copy import deepcopy

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

class Letter:

    def __init__(self, letter):
        """
        --------------------------------------------------------
        Initializes a letter object.
        Use: l = Letter(letter)
        --------------------------------------------------------
        Parameters:
            letter - A character from the alphabet (char)
        Returns:
            A new Letter object
        --------------------------------------------------------
        """
        self._letter = letter
        self._count = 0
        return

    def __str__(self):
        """
        --------------------------------------------------------
        A Python magic method that returns the string
        representation of the Letter object.
        Use: print(l)
        Use: str(l)
        --------------------------------------------------------
        Parameters:
            None
        Returns:
            A formatted version of all contents in Letter (str)
        --------------------------------------------------------
        """
        return "({:}, {:})".format(self._letter, self._count)

    def __eq__(self, char):
        """
        --------------------------------------------------------
        Compares a character in the alphabet to the letter in
        the Letter object.
        Use: l == char
        --------------------------------------------------------
        Parameters:
            char - A character from the alphabet (char)
        Returns:
            True - char is equal to the letter
            False - char is not equal to the letter
        --------------------------------------------------------
        """
        return self._letter == char

    def count(self):
        """
        --------------------------------------------------------
        Returns the number of times this Letter appears in a
        string of text
        Use: num = l.count()
        --------------------------------------------------------
        Parameters:
            None
        Returns:
            Letter frequency (int)
        --------------------------------------------------------
        """
        return self._count

    def increment(self):
        """
        --------------------------------------------------------
        Increments the Letter count by 1
        Use: l.increment() 
        --------------------------------------------------------
        Parameters:
            None
        Returns:
            None
        --------------------------------------------------------
        """
        self._count += 1

    def char(self):
        """
        --------------------------------------------------------
        Returns a copy of the character in the Letter object
        Use: c = l.char()
        --------------------------------------------------------
        Parameters:
            None
        Returns:
            A copy of the character in this object (char)
        --------------------------------------------------------
        """
        return deepcopy(self._letter)

class LetterCount:

    def __init__(self):
        """
        --------------------------------------------------------
        Initializes a LetterCount object, which contains a
        list of Letter objects using the entire lowercase
        alphabet.
        Use: lc = LetterCount()
        --------------------------------------------------------
        Parameters:
            None
        Returns:
            A new LetterCount object (LetterCount)
        --------------------------------------------------------
        """
        self._letters = []

        for x in ALPHABET:
            self._letters.append(Letter(x))
        
        return

    def add(self, char):
        """
        --------------------------------------------------------
        Increments the count of the provided character
        Use: lc.add(char)
        --------------------------------------------------------
        Parameters:
            char - A letter (char)
        Returns:
            None
        --------------------------------------------------------
        """

        index = ALPHABET.find(char)
        self._letters[index].increment()

    def add_word(self, word):
        """
        --------------------------------------------------------
        Increments the counts of all the characters inside word
        Use: lc.add_word(word)
        --------------------------------------------------------
        Parameters:
            word - A word (str)            
        Returns:
            None
        --------------------------------------------------------
        """
        for x in word:
            self.add(x)

    def get_count(self, char):
        """
        --------------------------------------------------------
        Gets the count of the provided character
        Use: num = lc.get_count(char)
        --------------------------------------------------------
        Parameters:
            char - a character from the alphabet (char)
        Returns:
            The count of char (int)
        --------------------------------------------------------
        """

        index = ALPHABET.find(char)

        return self._letters[index].count()

    def get_count_except(self, char):
        """
        --------------------------------------------------------
        Adds all of the counts together except for the provided
        char
        Use: num = lc.get_count_except(char) 
        --------------------------------------------------------
        Parameters:
            char - a character from the alphabet (char)
        Returns:
            The count of all characters except char (int)
        --------------------------------------------------------
        """

        count = 0

        for letter in self._letters:
            if(letter != char):
                count += letter.count()

        return count

    def get_letters(self):
        """
        --------------------------------------------------------
        Returns the list of Letters in this object
        Use: letters = lc.get_letters()
        --------------------------------------------------------
        Parameters:
            None
        Returns:
            A list of Letter objects (Letter[])
        --------------------------------------------------------
        """

        return self._letters


    def __str__(self):
        """
        --------------------------------------------------------
        Returns the string representation of the LetterCount
        object.
        Use: str(lc)
        Use: print(lc)
        --------------------------------------------------------
        Parameters:
            None
        Returns:
            A formatted version of the LetterCount object (str)
        --------------------------------------------------------
        """
        
        output = ""

        for letter in self._letters:
            output += str(letter) + "\n"

        return output
"""
--------------------------------------------------------
Title:      Wordle Guesser
File Name:  Characters.py
Author:     Matt McBurnie
Version:    1.0.0
Date:       February 26, 2022
--------------------------------------------------------
"""

from copy import deepcopy
import enum

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

class Letter:

    def __init__(self, letter):
        """
        --------------------------------------------------------
        Creates a new Letter object with the character along
        with the minimum amount and the maximum amount
        Use: l = Letter(letter)
        --------------------------------------------------------
        Parameters:
            letter - a character from the alphabet (char)
        Returns:
            A new Letter object
        --------------------------------------------------------
        """
        self.letter = letter
        self._min_count = 0
        self._max_count = 5

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
        return "({:}, {:}, {:})".format(self.letter, self._min_count, self._max_count)

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
        return char == self.letter

    def decrement(self):
        """
        --------------------------------------------------------
        Decreases the max possible characters by 1.
        Use: l.decrement()
        --------------------------------------------------------
        Parameters:
            None
        Returns:
            None
        --------------------------------------------------------
        """
        self._max_count -= 1

        if(self._max_count == 0):
            self._min_count = 0
        return
    
    def increment(self):
        """
        --------------------------------------------------------
        Increases the min possible characters by 1
        Use: l.increment()
        --------------------------------------------------------
        Parameters:
            None
        Returns:
            None
        --------------------------------------------------------
        """
        self._min_count += 1
        return

    def set_max(self, amount):
        """
        --------------------------------------------------------
        Sets the max possible characters to [amount]
        Use: l.set_max(amount)
        --------------------------------------------------------
        Parameters:
            amount - a number (int)
        Returns:
            None
        --------------------------------------------------------
        """
        self._max_count = amount

        if(self._max_count == 0):
            self._min_count = 0

        return

    def set_min(self, amount):
        """
        --------------------------------------------------------
        Sets the min amount of characters to [amount]
        Use: l.set_min(amount)
        --------------------------------------------------------
        Parameters:
            amount - a number (int)
        Returns:
            None
        --------------------------------------------------------
        """
        self._min_count = amount
        return

    def get_min(self):
        """
        --------------------------------------------------------
        Returns a copy of the min value of this Letter
        Use: l.get_min()
        --------------------------------------------------------
        Parameters:
            None
        Returns:
            None
        --------------------------------------------------------
        """
        return deepcopy(self._min_count)
    
    def get_max(self):
        """
        --------------------------------------------------------
        Returns a copy of the max value of this Letter
        Use: l.get_max()
        --------------------------------------------------------
        Parameters:
            None
        Returns:
            None
        --------------------------------------------------------
        """
        return deepcopy(self._max_count)
    

class Letters:

    def __init__(self):
        """
        --------------------------------------------------------
        Creates a new Letters object containing a list of 
        Letter objects using the entire lowercase alphabet.
        Use: l = Letters()
        --------------------------------------------------------
        Parameters:
            None
        Returns:
            A new Letters object (Letters)
        --------------------------------------------------------
        """
        self.letters = []

        for x in ALPHABET:
            self.letters.append(Letter(x))

        return

    def __str__(self):
        """
        --------------------------------------------------------
        Returns a string representation of the Letters object.
        Use: str(l)
        Use: print(l)
        --------------------------------------------------------
        Parameters:
            None
        Returns:
            A formatted version of the Letters object (str)
        --------------------------------------------------------
        """

        letters = ""

        for i, letter in enumerate(self.letters):

            if(letter.get_max() > 0):
                letters += "{:}    ".format(letter)
            else:
                letters += "---------    "

            if((i + 1) % 4 == 0):
                letters += "\n"
            
        

        return letters

    def __contains__(self, char):
        """
        --------------------------------------------------------
        A Python magic method that allows the use of the 'in'
        operator
        Use: char in l 
        --------------------------------------------------------
        Parameters:
            char - A character in the alphabet (char)
        Returns:
            True - char has a max count greater than 0
            False - char has a max count equal to 0
        --------------------------------------------------------
        """

        output = False

        for letter in self.letters:
            if(char == letter and letter.get_max() > 0):
                output = True
                break
        
        return output
    
    def __getitem__(self, i):
        """
        --------------------------------------------------------
        A Python magic method that allows you to treat Letters
        like a list structure
        Use: l[i]
        --------------------------------------------------------
        Parameters:
            i - The index of the Letter (int)
        Returns:
            The Letter object at index i (Letter)
        --------------------------------------------------------
        """
        return self.letters[i]

    def __iter__(self):
        """
        --------------------------------------------------------
        A Python magic method that allows you to iterate through
        a list.
        Use: for x in l
        --------------------------------------------------------
        Parameters:
            None
        Returns:
            yields values in the list of Letter objects.
        --------------------------------------------------------
        """

        for x in self.letters:
            yield x

    def decrement_letter(self, char): 
        """
        --------------------------------------------------------
        Decreases the max count of char by 1
        Use: l.decrement_letter(char)
        --------------------------------------------------------
        Parameters:
            char - the character in the alphabet (char)
        Returns:
            None
        --------------------------------------------------------
        """
        index = ALPHABET.find(char)

        if(self.letters[index].get_min() < self.letters[index].get_max()):
            self.letters[index].decrement() 

    def decrement_except(self, char):
        """
        --------------------------------------------------------
        Decrements all max counts by 1 except for char
        Use: l.decrement_except(char)
        --------------------------------------------------------
        Parameters:
            char - the character in the alphabet (char)
        Returns:
            None
        --------------------------------------------------------
        """

        for letter in ALPHABET:
            if(char != letter):
                self.decrement_letter(letter)

    def decrement_all(self):
        """
        --------------------------------------------------------
        Decrements all max counts by 1
        Use: l.decrement_all()
        --------------------------------------------------------
        Parameters:
            None
        Returns:
            None
        --------------------------------------------------------
        """
        for letter in ALPHABET:
            self.decrement_letter(letter)

    def increment_letter(self, char):
        """
        --------------------------------------------------------
        Increments the min count of char by 1
        Use: l.increment_letter(char)
        --------------------------------------------------------
        Parameters:
            char - the character in the alphabet (char)
        Returns:
            None
        --------------------------------------------------------
        """
        index = ALPHABET.find(char)
        self.letters[index].increment()

    def set_max_letter(self, char, amount):
        """
        --------------------------------------------------------
        Sets the max count of char to [amount]
        Use: l.set_max_letter(char, amount)
        --------------------------------------------------------
        Parameters:
            char - the character in the alphabet (char)
            amount - a number to set the max count to (int)
        Returns:
            None
        --------------------------------------------------------
        """
        index = ALPHABET.find(char)
        minimum = self.get_min(char)
        if(minimum != 0 and amount < minimum):
            self.letters[index].set_max(minimum)
        else:
            self.letters[index].set_max(amount)

    def set_min_letter(self, char, amount):
        """
        --------------------------------------------------------
        Sets the min count of char to [amount]
        Use: l.set_min_letter(char, amount)
        --------------------------------------------------------
        Parameters:
            char - the character in the alphabet (char)
            amount - a number to set the min count to (int)
        Returns:
            None
        --------------------------------------------------------
        """
        index = ALPHABET.find(char)
        self.letters[index].set_min(amount)


    def set_max_letters_except(self, char, amount):
        """
        --------------------------------------------------------
        Sets the max count of all letters to [amount] except
        char
        Use: l.set_max_letters_except(char, amount) 
        --------------------------------------------------------
        Parameters:
            char - the character in the alphabet (char)
            amount - a number to set the max count to (int)
        Returns:
            None
        --------------------------------------------------------
        """

        for letter in ALPHABET:
            if(letter != char):
                self.set_max_letter(letter, amount)

    def get_max(self, char):
        """
        --------------------------------------------------------
        Gets the max count of char
        Use: num = l.get_max(char)
        --------------------------------------------------------
        Parameters:
            char - the character in the alphabet (char)
        Returns:
            The Letter's max count (int)
        --------------------------------------------------------
        """
        index = ALPHABET.find(char)
        return self.letters[index].get_max()
    
    def get_min(self, char):
        """
        --------------------------------------------------------
        Gets the min count of char
        Use: num = l.get_min(char)
        --------------------------------------------------------
        Parameters:
            char - the character in the alphabet (char)
        Returns:
            The Letter's min count (int)
        --------------------------------------------------------
        """
        index = ALPHABET.find(char)
        return self.letters[index].get_min()
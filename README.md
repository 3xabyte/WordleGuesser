# What is Wordle?

Wordle is a game made by Josh Wardle. Users have 6 attempts to get the 5 letter word of the day. Each guess the user makes, the game gives the user feedback by using gray, yellow, and green squares. See the table below to see what each square means

| Color  | Information                                                  |
| ------ | ------------------------------------------------------------ |
| Green  | The character exists in the word AND the character is in the correct position |
| Yellow | The character exists in the word BUT the character is not in the correct position |
| Gray   | The character does not exist in the word                     |

There are also useful patterns that help the user determine what the word is, such as having one green letter and one gray letter. Let 'e' be the one green and one gray letter. This tells the user that there is exactly one 'e' in the word and the one 'e' that is green is in the correct spot. 



# What is WordleGuesser?

WordleGuesser is a program that helps the user find the word of the day faster. By utilizing the information from the user's guesses, the program will eliminate words that do not meet the requirements. 



## How does WordleGuesser work?

WordleGuesser starts by asking for the user's guess. The program then asks the user to enter the guess again, except that all yellow characters and gray characters are replaced by dashes. A similar process is used for the yellow characters as well. 

By utilizing the information from the user, the program will do the following:



### (1) Process Greens

The program loops through the green characters. Any green character will delete all other possible characters in a list at that position. 

Example: if my guess is `power` and the green characters are `p----`, the possible character list at index 0 will just be ['p']. The possible character lists at indexes 1 to 4 will still contain all the other characters, at least for now.



### (2) Process Yellows

The program loops through the yellow characters. Any yellow character will be deleted from its own list of possible characters at that index. 

Example: If my guess is `power` and the yellow characters are `---e-`, the possible character list at index 3 will contain all the characters of the alphabet, except e. The remaining lists are not impacted.



### (3) Process Grays

The program goes through the remaining characters. Any gray character will be deleted from all lists of possible characters.

Example: If my guess is `power`, where the green characters are `p----` and the yellow characters are `---e-`, 'o', 'w', 'r' will be removed from all the lists of possible guesses.



### (4) Update Counts

The program goes through every character and updates the count based on the information from the user. The minimum frequency of the characters increases to the amount inside both the greens and the yellows. The maximum frequency of the characters decreases by the amount of green characters and the yellow characters. The maximum frequency can also decrease to the minimum frequency if that character is gray. 



## Other Functions in WordleGuesser

There are a few other minor functions in WordleGuesser. Examples include printing the remaining possible words on screen and printing the remaining characters on screen. WordleGuesser prints the remaining possible words either to the console and to the possible_words.txt file. 

# Guessing Game

In a file called `game.py`, implement a program that:

* Prompts the user for a level, `n`. If the user does not input a positive integer, the program should prompt again.
* Randomly generates an integer between `1` and `n`, inclusive, using the random module.
* Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
  * If the guess is smaller than that integer, the program should output `Too small!` and prompt the user again.
  * If the guess is larger than that integer, the program should output `Too large!` and prompt the user again.
  * If the guess is the same as that integer, the program should output `Just right!` and exit.
# Blackjack Game

This is a simplified version of blackjack where we're only going to have 
a computer dealer and a human player and a deck of 52 cards.

* The human player has a bank roll from which they place a bet indicating whether or not they think
they're going to win this set of hands.

* The player starts with two cards face up and the dealer starts with one card face up and one card face down.

* The player goes first in the gameplay and the player goal is to get closer
to a total value of 21 than the dealer does.

* The total value is just the sum of the current face up cards the human player has.

* There are two possible actions that a human player can take.

    * They can either hit, which is to receive another card from the deck, 
    or 
    * they can stay to stop receiving cards.

All the player has to be able to do is hit, which is to take a card from the deck
and put it in their hand and then take a new sum there, or stay.

The game can end in the following ways:

- If the player keeps hitting before the computer even goes, and they go over 21, then they bust and lose their bet.

- The second way the game can end is if the player beats the dealer.
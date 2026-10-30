# AI DEVELOPMENT LOG
#
# Copilot Prompt 1: We are going to build a blackjack game in python that runs on the terminal, the executable must be named blackjack.py
#
# Copilot Prompt 2: 
#
# Copilot Prompt 3:
#
## All the code was generated with one prompt.
#
# One problem or bug I encountered: No bugs found. The game was too fasted paced.
#
# How I fixed it: I added a pause function to work in between each drawn hand.
#
# One change I made myself without Copilot: Added symbols to each card suit. Added pause function and implemented it on the code.
#
# One thing I learned about the Python code: It is a very simple language but can be very well structured, I had little struggle with following the code because of its complex design.
#
# 1. The (hand_value(hand)) function calculates the value of a Blackjack hand by going through each card in the hand and adding its value to a total.
#
# 2. The ace is counted as 11 initially, but if the total value exceeds 21, it is counted as 1 instead.
#
# 3. No compromising problems. Code had 1 design inconvenience, game was too fast paced, so I added pause function.
#
#!/usr/bin/env python3
"""A small terminal blackjack game."""

import random
import time



SUITS = ("♥ Hearts", "♦ Diamonds", "♣ Clubs", "♠ Spades")
RANKS = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")


def pause():
    #Pause for a moment to let the player read the output.
    time.sleep(1.5)

def create_deck():
    """Return a shuffled standard deck represented as (rank, suit) pairs."""
    deck = [(rank, suit) for suit in SUITS for rank in RANKS]
    random.shuffle(deck)
    return deck


def hand_value(hand):
    """Return the best blackjack value for a hand, counting aces as needed."""
    value = 0
    aces = 0
    for rank, _ in hand:
        if rank in ("J", "Q", "K"):
            value += 10
        elif rank == "A":
            value += 11
            aces += 1
        else:
            value += int(rank)

    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value


def hand_text(hand):
    """Format cards for display in the terminal."""
    return ", ".join(f"{rank} of {suit}" for rank, suit in hand)


def show_hand(label, hand, hide_first=False):
    """Print a hand, optionally hiding its first card."""
    if hide_first:
        cards = ["Hidden card"] + [f"{rank} of {suit}" for rank, suit in hand[1:]]
        print(f"{label}: {', '.join(cards)}")
    else:
        pause()
        print(f"{label}: {hand_text(hand)} (value: {hand_value(hand)})")


def player_turn(deck, player_hand, dealer_hand):
    """Run the player's choices and return whether the player busted."""
    while True:
        show_hand("Dealer", dealer_hand, hide_first=True)
        show_hand("Your hand", player_hand)

        if hand_value(player_hand) > 21:
            print("You busted.")
            return True

        choice = input("Hit or stand? [h/s]: ").strip().lower()
        if choice in ("h", "hit"):
            player_hand.append(deck.pop())
        elif choice in ("s", "stand"):
            return False
        else:
            print("Please enter h to hit or s to stand.")


def dealer_turn(deck, dealer_hand):
    """Deal to the house until its hand is worth at least 17."""
    while hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
        pause()


def play_round():
    """Play one round and print its result."""
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    pause()
    print("\n" + "=" * 40)
    print("New round")
    print("=" * 40)
    pause()

    if hand_value(player_hand) == 21:
        show_hand("Dealer", dealer_hand, hide_first=True)
        show_hand("Your hand", player_hand)
        if hand_value(dealer_hand) == 21:
            show_hand("Dealer", dealer_hand)
            print("Push: both hands are blackjack.")
        else:
            show_hand("Dealer", dealer_hand)
            print("Blackjack! You win.")
        return
        pause()

    if player_turn(deck, player_hand, dealer_hand):
        show_hand("Dealer", dealer_hand)
        return


    dealer_turn(deck, dealer_hand)
    show_hand("Dealer", dealer_hand)
    show_hand("Your hand", player_hand)

    player_value = hand_value(player_hand)
    dealer_value = hand_value(dealer_hand)
    if dealer_value > 21:
        print("Dealer busted. You win!")
    elif player_value > dealer_value:
        print("You win!")
    elif player_value < dealer_value:
        print("Dealer wins.")
    else:
        print("Push: tie game.")


def main():
    """Run rounds until the player chooses to quit."""
    print("Welcome to Blackjack!")
    while True:
        play_round()
        choice = input("\nPlay again? [y/n]: ").strip().lower()
        if choice not in ("y", "yes"):
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
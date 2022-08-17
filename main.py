import pydealer
import sys
import time
from pydealer.const import POKER_RANKS
from blessed import Terminal
t = Terminal()

print("Console Texas Holdem!")
time.sleep(1)
print("1. Play")
time.sleep(1)
print("2. Exit")
time.sleep(1)
op1 = input("Choose a option: ")
op1 = int(op1)
if op1 == 1:
  print("lets play!")

elif op1 == 2:
  print("sorry to see you go!")
  sys.exit()




chips = 1000
deck = pydealer.Deck()
hand = pydealer.Stack()
discard_p = pydealer.Stack()
flop = pydealer.Stack()

deck.shuffle()

top_card = deck.deal(1)
print("You have", chips, "poker chips")
chips -= 1
time.sleep(1)
print("You place the ante and now have", chips, "poker chips")
discard_p.add(top_card)
time.sleep(1)
print("The dealer burns the top card")
p1cards = deck.deal(2)
time.sleep(1)
print("The dealer deals the cards")
hand.add(p1cards)
hand.sort()
time.sleep(1)
print("Your cards are:")
print(t.blue(str(hand)))
time.sleep(1)
first_bet = input("How much would you like to bet? ")
first_bet = int(first_bet)
chips -= first_bet
if chips < first_bet:
  print("ur broke noob")
  sys.exit()
time.sleep(1)
print("You bet", first_bet, "poker chips, and have", chips, "poker chips left")
nextTopCard = deck.deal(1)
discard_p.add(nextTopCard)
time.sleep(1)
print("The dealer burns the top card")
addFlop = deck.deal(3)
flop.add(addFlop)
flop.sort()
time.sleep(1)
print("The dealer lays out the flop")
time.sleep(1)
print("The cards in the flop are:")
print(t.green(str(flop)))
time.sleep(1)
second_bet = input("How much would you like to bet(or fold)? ")
if second_bet.equals("fold"):
  print("You fold")
  sys.exit()

second_bet = int(second_bet)
chips -= second_bet
if chips < second_bet:
  print("ur broke noob")
  sys.exit()

time.sleep(1)
print("You bet", second_bet, "poker chips, and have", chips, "poker chips left")
time.sleep(1)
turn = deck.deal(1)
flop.add(turn)
flop.sort()
time.sleep(1)
print("The dealer lays out the turn, the flop is now:")
print(t.green(str(flop)))
time.sleep(1)
third_bet = input("How much would you like to bet? ")
if third_bet.contains("fold"):
  print("You fold")
  sys.exit()

third_bet = int(third_bet)
chips -= third_bet
if chips < third_bet:
  print("ur broke noob")
  sys.exit()
time.sleep(1)
print("You bet", third_bet, "poker chips, and have", chips, "poker chips left")
time.sleep(1)
river = deck.deal(1)
flop.add(river)
flop.sort()
time.sleep(1)
print("The dealer lays out the river card, the flop is now:")
print(t.green(str(str)))
time.sleep(1)
four_bet = input("How much would you like to bet? ")
four_bet = int(four_bet)
chips -= four_bet
if chips < four_bet:
  print("ur broke noob")
  sys.exit()
time.sleep(1)
print("You bet", four_bet, "poker chips, and have", chips, "poker chips left")
time.sleep(1)



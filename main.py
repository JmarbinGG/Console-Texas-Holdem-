import pydealer
import sys

print("Console Texas Holdem!")
print("1. Play")
print("2. Exit")
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

deck.shuffle()

top_card = deck.deal(1)
print("You have", chips, "poker chips")
chips -= 1
print("You place the ante and now have", chips, "poker chips")
discard_p.add(top_card)
print("The dealer burns the top card")
p1cards = deck.deal(2)
print("The dealer deals the cards")
hand.add(p1cards)
print("Your cards are:", hand)

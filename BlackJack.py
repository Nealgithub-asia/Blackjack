import random

def hiddencard():
    card=["?","?"]
    return card

def cardpresent(card):
    suit=card[0]

    if suit == "?":
        print("""
    ┌─────────┐
    │░░░░░░░░░│
    │░░░░░░░░░│
    │░░░ ? ░░░│
    │░░░░░░░░░│
    │░░░░░░░░░│
    └─────────┘""")
        return
    suit_sym = {"diamonds": "♦", "spades": "♠", "hearts": "♥", "clubs": "♣"}
    symbol = suit_sym[suit]
    rank = str(card[1])

    #below code is to ensure space for 1 and 2 digit characters, if its one digit the code will add a space otherwise not
    if len(rank) == 2:
        space = "" 
    else:
        space = " "

    print(f"""
    ┌─────────┐
    │{rank}{space}       │
    │         │
    │    {symbol}    │
    │         │
    │       {space}{rank}│
    └─────────┘""",end="")

class deck:
    def __init__(self):
        pass

    def fill(cards):
        for suit in suits:
            for rank in ranks:
                cards.append([suit, rank])
        
    def shuffle(list):
        return random.shuffle(list)

    def deal(number):
        cards_dealt=[]
        
        for i in range(number):
            card=cards.pop()
            cards_dealt.append(card)

        return cards_dealt 

class hand:
    
    def __init__(self, initial_cards):
        self.cards=initial_cards
        
    def hit(self):
        self.cards.append(cards.pop())
        for card in self.cards:
            cardpresent(card)
        print(f"Total value {self.value()}") 
    def value(self):
        val=0
        aces=0
        for card in self.cards:
            val+=ranks[card[1]]  #key= card[1]
            if card[1]=="A":
                aces+=1        

        while val>21 and aces>0:
            val-=10
            aces-=1

        return val

def computerlogic():
    print("Computer cards")
    for card in comp_hand.cards:
        cardpresent(card)

    if comp_hand.value()<=16:
        while comp_hand.value()<=16:
            print("\nDealer hits!")
            comp_hand.hit()
    else:
        for card in comp_hand.cards:
            cardpresent(card)
        print(f"Total value {comp_hand.value()}") 
cards=[] 
suits=["diamonds", "spades", "hearts", "clubs"]
ranks={"A": 11,2: 2,3: 3,4: 4,5: 5,6: 6,7: 7,8: 8,9: 9,10: 10,"J": 10,"Q": 10 ,"K": 10}

deck.fill(cards)
deck.shuffle(cards)

user_hand=hand(deck.deal(2))
print("Your cards: ")
for card in user_hand.cards:
    cardpresent(card)
print(f"Total value {user_hand.value()}") 

comp_hand=hand(deck.deal(2))
print("computer cards:")
cardpresent(comp_hand.cards[0])
cardpresent(hiddencard())

while(1):
    print("<<<<<<<<<<Hit or Stand>>>>>>>>>>")
    opt=input().lower()
    if opt=="hit":
        user_hand.hit()
        if(user_hand.value()>21):
            print("bust!")
            break
    elif opt=="stand":   
        break
print("<<<<<<<<<<Dealer's turn>>>>>>>>>>")
computerlogic()

user_val=user_hand.value()
comp_val=comp_hand.value()

if user_val > 21:
    print("You lost! (Bust)")
elif comp_val > 21:
    print("You win! (Computer Bust)")
elif user_val > comp_val:
    print("You win!")
elif user_val == comp_val:
    print("Push! (Tie)")
else:
    print("You lost!")
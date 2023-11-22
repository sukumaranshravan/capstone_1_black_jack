import random
cards=[1,2,3,4,5,6,7,8,9,10,'K','J','Q','A']

player_point=[]
dealer_point=[]

for i in range(2):
    player_hand=random.choice(cards)
    player_point.append(player_hand)
    dealer_hand=random.choice(cards)
    dealer_point.append(dealer_hand)
print(f"Player Cards :{player_point}")
print(f"Dealer Card :{dealer_point[0]}")

def stay():
    while len(dealer_point)<len(player_point):
        dealer_hand=random.choice(cards)
        dealer_point.append(dealer_hand)
    print(f"Dealer :{dealer_point}")
    return dealer_point
def hit():
    player_hand=random.choice(cards)
    player_point.append(player_hand)
    print(f"Player :{player_point}")
    return player_point

go_on=True
while go_on:
    deal=input("Hit or Stay, y/n")
    if deal=='y':
        hit()
        hands_player=len(player_point)
    else:
        stay()
        go_on=False

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

def player_point_counter():
    score_player=0
    for i in player_point:
        if i=='K' or i=='J' or i=='Q':
            score_player+=10
        elif i=='A':
            if score_player<=10:
                score_player+=11
            else:
                score_player+=1
        else:
            score_player+=i
    return score_player

def dealer_point_counter():
    score_dealer=0
    for i in dealer_point:
        if i=='K' or i=='J' or i=='Q':
            score_dealer+=10
        elif i=='A':
            if score_dealer<=10:
                score_dealer+=11
            else:
                score_dealer+=1
        else:
            score_dealer+=i    
    return score_dealer
x=player_point_counter()
y=dealer_point_counter()
# print(f"Player{x}")
# print(f"Dealer{y}")
if x>y and x<=21:
    print(f"You Win with {x} points")
else:
    print(f"Dealer Wins with {y} points")

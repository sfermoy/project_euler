
##############################definations################################

def high_card(hand_A,hand_B):
	hand_A.reverse()
	hand_B.reverse()
	for i in range(0,5):
		if hand_A[i][0]>hand_B[i][0]:
			return 1
		elif hand_B[i][0]>hand_A[i][0]:
			return 0

def is_flush(hand):
	for i in range(0,5):
		if hand[0][1]!=hand[i][1]:
			return False
	return True

#hand_3=[["1","C"],["1","C"],["1","C"],["1","C"],["1","C"]]
#print is_flush(hand_3)

def is_straight(hand):
	if hand[4][0]==14:
		for i in range(0,3):
			if hand[i][0]!=(hand[i+1][0]-1):
				return False
		if hand[0][0]==2:
			return True
		elif hand[3][0]==13:
			return True
		else:
			return False
	else:
		for i in range(0,4):
			if hand[i][0]!=(hand[i+1][0]-1):
				return False
		return True

#hand_3=[["2","C"],["3","C"],["4","C"],["5","C"],["14","C"]]
#hand_4=[["7","C"],["8","C"],["9","C"],["10","C"],["11","C"]]

#print is_flush(hand_3)
#print is_flush(hand_4)

def non_str8_or_flush_val(hand):
	combinations=[]
	consecutive=1

	for i in range(0,4):
		if hand[i][0]==(hand[i+1][0]):
			consecutive+=1	

			#only used in one pair case
			one_pair_val=hand[i][0]
		else:
			combinations.append(consecutive)
			consecutive=1
	combinations.append(consecutive)

	if len(combinations)==2:
		#either 4kind or house
		if max(combinations)==4:
			#4kind
			return [7,hand[3][0]]
		else:
			#full house
			if hand[2][0]==hand[4][0]:
				return[6,hand[2][0],hand[0][0]]
			else:
				return[6,hand[2][0],hand[4][0]]

	elif len(combinations)==3:
		#either 2p or trips
		if max(combinations)==3:
			#trips
			return [3,hand[2][0]]
		else:
			#2p
			pairs=[hand[1][0],hand[3][0]]
			return [2,max(pairs),min(pairs)]
	
	elif len(combinations)==4:
		return [1,one_pair_val]

	else:
		#high card
		return [0]
	
def hand_value(hand):
	#value=[0,0]
	if is_flush(hand):
		if is_straight(hand):
			#straight flush
			return [8,hand[3][0]]
		#flush
		return [5,hand[4][0]]
	
	elif is_straight(hand):
		#straight
		return [4,hand[[3][0]]]

	else:
		return non_str8_or_flush_val(hand)

	
def compare_hands(hand_A,hand_B):
	hand_A_value = hand_value(hand_A)
	hand_B_value = hand_value(hand_B)

	for i in range(0,len(hand_A_value)):
		if hand_A_value[i]>hand_B_value[i]:
			return 1
		elif hand_A_value[i]<hand_B_value[i]:
			return 0
	return high_card(hand_A,hand_B)
	

############################----MAIN----########################################
# setup
read= open("/home/shane/Code/python/puzzle/project_euler/poker.txt","r")
session=read.readlines()
read.close()

# card_map is a dictionary that allows the mapping of the card value from strings to ints
card_map=[(str(x),x) for x in range(1,10)]
card_map.append(("T",10))
card_map.append(("J",11))
card_map.append(("Q",12))
card_map.append(("K",13))
card_map.append(("A",14))
card_map=dict(card_map)

#print card_map["Q"]
#print card_map["4"]

results=[]
for game in session:
	#print game
	my_game=game
	my_game=my_game.split()
	cards=[list(val_suit) for val_suit in my_game]

	#print cards
	for card in cards:
		card[0]=card_map[card[0]]
	
	hand_1 = cards[:5]#first 5 cards
	hand_2 = cards[5:]#last 5 cards
	hand_1.sort()
	hand_2.sort()

	ans=compare_hands(hand_1,hand_2)
	results.append(ans)
	#print hand_1,"\n", hand_2,"\n",ans,"\n\n"

totes=0
for n in results:
	if n==1:
		totes+=1
print totes
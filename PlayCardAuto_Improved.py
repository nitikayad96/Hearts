from random import randit

class Auto:
	def __init__(self):
		pass

	def auto(Player,sofar):
		cards = Player.hand
		clubs = []
		diamonds = []
		spades = []
		hearts = []
		for i in range(13):
			if cards[i]/13 == 0:
				clubs.append(cards[i])
			if cards[i]/13 == 1:
				diamonds.append(cards[i])
			if cards[i]/13 == 2:
				spades.append(cards[i])
			if cards[i]/13 == 3:
				hearts.append(cards[i])
		all_cards = [clubs,diamonds,spades,hearts]

		if len(sofar)==0:
			indices = []
			lowest = []
			for i in all_cards:
				if len(i)>0:
					lowest.append(i[0]%13)
					indices.append(all_cards.index(i))

			'''
			What to do if you have multiple suits with the same value card
			Randomly selects a suit to play
			'''
			if lowest.count(min(lowest)) > 1:
				index_repeat = []
				for i in lowest:
					if i == min(lowest):
						index_repeat.append(indices[lowest.index(i)])

				r = randint(0,len(index_repeat)-1)
				index_rand = index_repeat[r]
				play = all_cards[index_rand][0]
				all_cards[index_rand].pop(0)
	
			else:
				min_index = lowest.index(min(lowest))
				play = all_cards[indices[min_index]][0]
				all_cards[indices[min_index]].pop(0)

		elif len(sofar)==3:
			card1, card2, card3 = sofar()



		







					






class Character():
	''' Base class for a character. '''
	cards = []
	items = []
	lives = 1
	
	def __init__(self, name):
		self.name = name
	
	def add_card(self, card):
		self.cards.append(card)

class Card():
	''' The base class for a card. ''' 
	damage = 0

	def __init__(self, name, damage):
		self.name = name
		self.damage = damage

class MeleeCard(Card):
	''' Child of the Card class, is melee. ''' 
		
	type = 'Melee'

	def __init__(self, name, damage, effect=None):
		''' A melee card, physical damage. ''' 
		super().__init__(name, damage)
		self.effect = effect
	

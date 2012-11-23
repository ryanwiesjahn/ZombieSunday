# Bullets
# Author list:
# 	Luke Martin <ltmartin@bsu.edu>
# 	Michael Milkovic <mlmilkovic@bsu.edu>
# 	Derek Onay <dsonay@bsu.edu>
# 	Ryan Wiesjahn <rwiesjahn@bsu.edu>

import somber as somber_engine
from weapon import *

class Bullet(somber_engine.Active):
	def __init__(self, somber, character, x=0, y=0):
		sprite = 'sprites/bullets/bullet_default.png'
		somber_engine.Active.__init__(self, sprite, somber=somber, pos=(x, y))
		character.level.add_object(self, 'bullets')
		self.hspeed = 600
		
		if character.direction == 0:
			self.hspeed = -self.hspeed
		
	def update(self):	
		somber_engine.Active.update(self)

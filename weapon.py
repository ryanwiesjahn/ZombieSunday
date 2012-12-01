# Handles weapons (duh)
# Author list:
# 	Luke Martin <ltmartin@bsu.edu>
# 	Michael Milkovic <mlmilkovic@bsu.edu>
# 	Derek Onay <dsonay@bsu.edu>
# 	Ryan Wiesjahn <rwiesjahn@bsu.edu>

import somber as somber_engine
from bullet import *
import items

class Weapon:
	def __init__(self, somber, character, attachments=[None, None]):
		self.somber = somber
		self.attachments = attachments
		self.type = WeaponType.Default
		self.character = character
		self.ammo = [0, 50]
		self.ammo[0] = self.ammo[1]
		self.rate = 0
		self.timer = self.rate
		
		self.set_weapon_type()
	
	def set_weapon_type(self):
		if self.attachments.count(Attachment.Speed) == 1:
			if self.attachments.count(Attachment.Fire) == 1:
				self.type = WeaponType.SpeedFire
				self.rate = 1
			elif self.attachments.count(Attachment.Lob) == 1:
				self.type = WeaponType.SpeedLob
				self.rate = 2
			elif self.attachments.count(Attachment.Force) == 1:
				self.type = WeaponType.SpeedForce
				self.rate = 2
			else:
				self.type = WeaponType.Speed
				self.rate = .2
	
		elif self.attachments.count(Attachment.Fire) == 1:
			if self.attachments.count(Attachment.Lob) == 1:
				self.type = WeaponType.FireLob
				self.rate = 2.5
			elif self.attachments.count(Attachment.Force) == 1:
				self.type = WeaponType.FireForce
				self.rate = 2
			else:
				self.type = WeaponType.Fire
				self.rate = 1
		
		elif self.attachments.count(Attachment.Lob) == 1:
			if self.attachments.count(Attachment.Force) == 1:
				self.type = WeaponType.LobForce
				self.rate = 2
			else:
				self.type = WeaponType.Lob
				self.rate = 2
				
		elif self.attachments.count(Attachment.Force) == 1:
				self.type = WeaponType.Force
				self.rate = 1.5
		
		elif self.attachments.count(Attachment.Speed) == 2:
			self.type = WeaponType.SpeedSpeed
			self.rate = 2
		
		elif self.attachments.count(Attachment.Fire) == 2:
			self.type = WeaponType.FireFire
			self.rate = -1
		
		elif self.attachments.count(Attachment.Lob) == 2:
			self.type = WeaponType.LobLob
			self.rate = 3
		
		elif self.attachments.count(Attachment.Force) == 2:
			self.type = WeaponType.ForceForce
			self.rate = 2
			
		elif self.attachments.count(None) == 2:
			self.type = WeaponType.Default
			self.rate = .5
		
		self.timer = self.rate
			
	def update(self, delta):
		self.weapon_timer(delta)
	
	def weapon_timer(self, delta):
		if self.timer < self.rate:
			self.timer += delta
		
	def fire(self):
		if self.rate >= 0:
			if self.timer >= self.rate:
				self.create_bullet()
				self.ammo[1] -= 1
				self.timer = 0
	
	def create_bullet(self):
		if self.type == WeaponType.Default:
			DefaultBullet(self.somber)
		elif self.type == WeaponType.Speed:
			SpeedBullet(self.somber)
		elif self.type == WeaponType.Fire:
			FireBullet(self.somber)
		elif self.type == WeaponType.Lob:
			LobBullet(self.somber)
		elif self.type == WeaponType.Force:
			ForceBullet(self.somber)
		else:
			DefaultBullet(self.somber)

	def set_ammo(self):
		if self.collides_with_group('items'):
			self.ammo[1] = 50
			
class WeaponType:
	Default, Speed, SpeedSpeed, SpeedFire, SpeedLob, SpeedForce, Fire, FireFire, FireLob, FireForce, Lob, LobLob, LobForce, Force, ForceForce = range(15)

class Attachment:
	Speed, Fire, Lob, Force = range(4)

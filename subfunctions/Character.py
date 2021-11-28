class Character:
	def __init__( self, name = '', charClass = '', attrib = [], subAttrib = [], \
						wounds = [], chips = [], arcaneAbilities = [], EandD = [], equipment = [], charNotes = '', gameNotes = '' ):
		#Inherent
		self.name = name;
		self.charClass = charClass;
		self.attrib = attrib;
		self.subAttrib = subAttrib;
		self.wounds = wounds;
		self.chips = chips;
		
		self.arcaneAbilities = arcaneAbilities;
		self.EandD = EandD;
		
		# Conditional
		self.equip = equipment;
		self.charNotes = charNotes;
		self.gameNotes = gameNotes;
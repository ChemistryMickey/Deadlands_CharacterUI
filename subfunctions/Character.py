class Character:
    def __init__( self, name = '', charClass = '', attrib = {}, subAttr = {}, \
                        wounds = [], chips = [], arcaneAbilities = [], edges = {}, hinders = {}, equipment = {}, charNotes = {}, gameNotes = {} ):
        #Inherent
        self.name = name;
        self.charClass = charClass;
        self.attrib = attrib;
        self.subAttr = subAttr;
        self.wounds = wounds;
        self.chips = chips;
        
        self.arcaneAbilities = arcaneAbilities;
        self.edges = edges;
        self.hinds = hinders;
        
        # Conditional
        self.equip = equipment;
        self.charNotes = charNotes;
        self.gameNotes = gameNotes;

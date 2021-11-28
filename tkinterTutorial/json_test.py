import json

# ~ class Specs:
	# ~ def __init__( self, specs = ['5000 Gb RAM', '5 PB SSD', '10 GHz Processor'] ):
		# ~ self.specs = specs;

class Laptop:
	def __init__(self, name = 'Default', cost = 0, specs = ['5000 Gb RAM', '5 PB SSD', '10 GHz Processor']):
		self.name = name;
		self.cost = cost;
		self.specs = specs;
		
laptop1 = Laptop('Chromebook', 200);

jsonStr = json.dumps( laptop1.__dict__ );

print( jsonStr );

# Debug
DEBUG_LEVELS = {'Error' : 0, 'Log' : 1, 'Debug' : 2}
DEBUG_LEVEL = DEBUG_LEVELS['Debug'];


attrAbr = ['C', 'D', 'K', 'M', 'N', 'Q', 'Sm', 'Sp', 'STR', 'V', 'Pace', 'Size', 'Wind', 'Grit'];
attributeLabels = ["Cognition", "Deftness", "Knowledge", "Mien", "Nimbleness", "Quickness", \
					"Smarts", "Spirit", "Strength", "Vigor", "Pace", "Size", "Wind", "Grit"];
					
subAtrAbr = ['artillery', 'arts', 'scrut', 'search', 'track', 'bow', 'filch', 'lockpick', 'shoot', 'sleight', 'speed', \
				 'throw', 'academia', 'area', 'demo', 'disguise', 'lang', 'mad', 'med', 'prof', 'sci', 'trade', 'animal', 'leader', 'overawe', \
				 'perform', 'persuade', 'tale', 'climb', 'dodge', 'drive', 'fight', 'horse', 'sneak', 'swim', 'team', 'quickDraw', 'bluff', \
				 'gamble', 'ridicule', 'scrounge', 'street', 'surivival', 'tinker', 'faith', 'guts']
subAttributeLabels = ["Artillery (Cog)", "Arts (Cog)", "Scrutinize (Cog)", "Search (Cog)", "Trackin' (Cog)", "Bow (Deft)", \
							"Filchin' (Deft)", "Lockpickin' (Deft)", "Shootin' (Deft)", "Sleight o' Hand (Deft)", "Speed Load (Deft)", \
							"Throwin' (Deft)", "Acadamia (Know)", "Area Knowledge (Know)", "Demolition (Know)", "Disguise (Know)", \
							"Language (Know)", "Mad Science (Know)", "Medicine (Know)", "Professional (Know)", "Science (Know)", \
							"Trade (Know)", "Animal Wranglin' (Mien)", "Leadership (Mien)", "Overawe (Mien)", "Performin' (Mien)", \
							"Persuasion (Mien)", "Tale Tellin' (Mien)", "Climbin' (Nimb)", "Dodge (Nimb)", "Drivin' (Nimb)", \
							"Fightin' (Nimb)", "Horse Ridin' (Nimb)", "Sneak (Nimb)", "Swimmin' (Nimb)", "Teamster (Nimb)", \
							"Quick Draw (Quick)", "Bluff (Smarts)", "Gamblin' (Smarts)", "Ridicule (Smarts)", "Scroungin' (Smarts)", \
							"Streetwise (Smarts)", "Survival (Smarts)", "Tinkerin' (Smarts)", "Faith (Spirit)", "Guts (Spirit)"];
                      
                      
woundLevels = ['None', 'Light', 'Heavy', 'Serious', 'Critical', 'Maimed'];
bodyPartLabels = ['Head', 'R. Arm', 'L. Arm', 'Guts', 'R. Leg', 'L. Leg'];
bodyPartAbbr = ['head', 'rarm', 'larm', 'guts', 'rleg', 'lleg'];
chipNames = ['White Chips', 'Red Chips', 'Blue Chips', 'Green Chips'];
chipTypes = ['white', 'red', 'blue', 'green'];
horseTypes = ['Ordinary', 'Brave', 'Fast', 'Smart', 'Strong', 'Surly', 'Tough'];
horseSkills = [val for i, val in enumerate( subAttributeLabels ) if i in [31, 34, 24, 45] ];
standardHorse = {
            'C' : '2d6', 'D' : '1d4', 'N' : '2d12', 'STR' : '2d10', 'Q' : '1d8', 'V' : '2d10', 
            "Fightin' (Nimb)" : '1d12', "Swimmin' (Nimb)" : '4d12', 'K' : '1d6', 'M' : '1d6', 
            'Sm' : '1d6', 'Sp' : '1d4', 'Guts (Spirit)' : '2d4', 'Overawe (Mien)' : '1d6', 'Terror' : '0',
            'Pace' : '20', 'Size' : '10', 'Wind' : '14/14'
        };
weaponAttrs = ['Item', 'Class', 'Shots', 'Ammo', 'Caliber', 'RoF', 'Damage', 'Range Increment', 'DB', 'Price'];

maxEandD = 5; #maximum number of edges and hinderances allowed. Determined by Marshal
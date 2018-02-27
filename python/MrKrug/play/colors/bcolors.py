class colors:
	def __init__(self):
		self.colorDict = {"PURPLE": '\033[95m',
    			"BLUE":'\033[94m',
			"GREEN":'\033[92m',
			"YELLOW":'\033[93m',
			"RED":'\033[91m'}

		self.styleDict = {"END":'\033[0m',
			"BOLD":'\033[1m',
			"UNDERLINE":'\033[4m'}

	def printColors(self):
		for c in self.colorDict:
			print(self.colorDict[c.upper()] + c + self.styleDict['END'])

	def printStyles(self):
		for s in self.styleDict:
			print(self.styleDict[s.upper()] + s + self.styleDict['END'])

	def setColor(self, color):
		for c in self.colorDict:
			if color.upper() == c:
				print(self.colorDict[c.upper()])

	def setStyle(self, style):
		for c in self.styleDict:
			if style.upper() == c:
				print(self.styleDict[c.upper()])


colorArray = ['PURPLE', 'BLUE', 'GREEN', 'YELLOW', 'RED']
styleArray = ['BOLD', 'UNDERLINE']
c = colors()

for color in colorArray:
	for style in styleArray:	
		c.setColor(color)
		c.setStyle(style)
		print("this is a pretty color... i suspect! And maybe underlined? Or bold?")
		c.setStyle('end')


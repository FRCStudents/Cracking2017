styleDict = {	"END":  '\33[0m',	
		"BOLD": '\33[1m',	
		"ITALIC":'\33[3m',	
		"UNDERLINE":'\033[4m'}	

colorDict = {	"BLACK":'\33[30m',	
		"RED":'\33[31m',	
		"GREEN":'\33[32m',	
		"YELLOW":'\33[33m',	
		"BLUE":'\33[34m',	
		"VIOLET":'\33[35m',	
		"CYAN":'\33[36m',	
		"WHITE":'\33[37m',	
		"GREY":'\33[90m',	
		"RED2":'\33[91m',	
		"GREEN2":'\33[92m',	
		"YELLOW2":'\33[93m',	
		"BLUE2":'\33[94m',	
		"VIOLET2":'\33[95m',	
		"CYAN2":'\33[96m',	
		"WHITE2":'\33[97m'}	

bgcolorDict = {	"BLACKBG":'\33[40m',   
		"REDBG":'\33[41m',     
		"GREENBG":'\33[42m',   
		"YELLOWBG":'\33[43m',  
		"BLUEBG":'\33[44m',    
		"VIOLETBG":'\33[45m',  
		"CYANBG":'\33[46m',   
		"WHITEBG":'\33[47m',  
		"GREYBG":'\33[100m',   
		"REDBG2":'\33[101m',   
		"GREENBG2":'\33[102m', 
		"YELLOWBG2":'\33[103m',        
		"BLUEBG2":'\33[104m',  
		"VIOLETBG2":'\33[105m',        
		"CYANBG2":'\33[106m', 
		"WHITEBG2":'\33[107m'}

line = "\t"
tab = "\t"
for bgcolor in bgcolorDict:
	print ("Background Color: " + bgcolor)
	for color in colorDict:
		for style in styleDict:
			if len(color) < 6:
				tab = "\t\t"
			else:
				tab = "\t"
			line += "[" + styleDict[style] + colorDict[color] + bgcolorDict[bgcolor] + color + styleDict['END'] + "]" + tab 
		print(line)
		line = "\t"

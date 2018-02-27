
import os
import webbrowser 

html = '<html> Generated stuff </html>'

path = os.path.abspath('temp.html')
url = 'file://' + path

with open(path, 'w') as f:
	f.write(html)

webbrowser.open(url)

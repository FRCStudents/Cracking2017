f = open('in.file', 'r')
for ln in f:
	l = ln.replace("my", "your")
	s = l.title().rstrip()
	s += " "  
	s += l.swapcase()
	print ("==> ", s)
f.close()

fin = open('in.file', 'r')
fout = open('outx.file', 'w')
fout.write(fin.read())
fin.close()
fout.close()
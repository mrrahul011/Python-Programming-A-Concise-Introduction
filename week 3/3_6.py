# -problem3_6.py *- coding: utf-8 -*-

import sys

infile = sys.argv[1]
outfile = sys.argv[2]

rfile = open(infile)
wfile = open(outfile,'w')
   
for line in rfile:
    line = line.strip('\n')
    wfile.write('%d\n' % len(line))

wfile.close()    
rfile.close()    





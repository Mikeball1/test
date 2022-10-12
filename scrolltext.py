import sys,time,os

def texttime(words):
	for c in words:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.1)
 
 
texttime("what is even going on im not paying attention\n")
texttime("what is a +b????????????\n")
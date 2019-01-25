import time

def progressBar(countPerObject, totalNumberObject, waitTime, object=None):
	if object == None:
		object = "█"
	else:
		if len(object) > 1:
			object = object[:1]
		
	for i in range(countPerObject*totalNumberObject):
		time.sleep(waitTime)
		progress = (object * ( int((i+1)/countPerObject )))
		emptySpace = (" " * (totalNumberObject - ( int((i+1)/countPerObject ) )) )
		percent = (i+1)
		print("|{:s}{:s}|\t{:d}% Complete".format(progress, emptySpace, percent), end="\r", flush=True)
	print()

progressBar(5,20,0.05,"*")
progressBar(1,50,0.04)
progressBar(10,10,0.02)

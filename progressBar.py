import time

#countPerObject = number of counts to make up 1 unit of object
#totalNumberObject = number of objects in the progress bar
#waitTime = time for each "tick"
#object = [OPTIONAL] object for your progress bar, default will be "█"

def progressBar(countPerObject, totalNumberObject, waitTime, object=None): #function to create progress bar
	if object == None: #checks if object contains nothing, apply default object for progress bar
		object = "█"
	else:
		if len(object) > 1: #checks string length for object, having nore than 1 character in object will mess up the progress bar
			object = object[:1] #formats object to only 1 character
		
	for i in range(countPerObject*totalNumberObject):
		time.sleep(waitTime)
		progress = (object * ( int((i+1)/countPerObject )))
		emptySpace = (" " * (totalNumberObject - ( int((i+1)/countPerObject ) )) )
		percent = (i+1)
		print("|{:s}{:s}|\t{:d}% Complete".format(progress, emptySpace, percent), end="\r", flush=True) #printing the progress bar
	print()

#Examples
progressBar(5,20,0.05,"*")
progressBar(1,50,0.04)
progressBar(10,10,0.02)

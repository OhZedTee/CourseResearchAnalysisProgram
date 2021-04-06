import pickle

class PickleToFile:
	def __init__(self,fileName):
		self.fileName = fileName

	def __str__(self):
		return("FileName: " + self.title + "\n")

	#This function will open up a new file (or overwite the file) and save the object to it
	def pickleObjectToFile(self, objectToPickle):
		file = open(self.fileName, "wb")
		pickle.dump(objectToPickle, file)
		file.close()

	#This function will return the object saved to the file
	def retrievePickledObject(self):
		file = open(self.fileName, "rb")
		pickleItems = pickle.load(file)
		file.close()
		return pickleItems

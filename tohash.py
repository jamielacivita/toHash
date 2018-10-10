import hashlib
import os

def getHash(filename):
	hasher = hashlib.md5()
	try:
		with open(filename, 'rb') as f:
			buf = f.read()
			hasher.update(buf)
		return hasher.hexdigest()
	except FileNotFoundError:
		return filename + " not found."

def getFiles(path):
	fileList = os.listdir(path)
	return fileList

def getNumberFiles(path):
	fileList = os.listdir(path)
	return len(fileList)

def main():
	import argparse

	parser = argparse.ArgumentParser()
	parser.add_argument("path")
	args = parser.parse_args()

	#print(args.filename)
	#print(getHash(args.filename))
	#print(ascii(getFiles(args.filename)))
	
	files = {}

	fileNumber = 1
	print("Number of files: " + str(getNumberFiles(args.path)))
	for f in getFiles(args.path):
		fileNumber = fileNumber + 1
		#if (fileNumber % 25 == 0):
			#print(fileNumber/getNumberFiles(args.path))
		h = getHash(args.path+f)
		n = ascii(f)
		
		if h in files:
			print(n + " is a duplicate.")
		else:
			files[h] = n


if (__name__=="__main__"):
	main()






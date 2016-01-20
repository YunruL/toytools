#-*- coding:utf-8 -*-
import random

class nonsense(object):
	def __init__(self,filename,chainLen=3):
		self.cache = {}
		self.filename = filename
		self.words = self.file_to_word()
		self.trainlength = len(self.words)
		self.chainLen = chainLen
		self.getCache()

	def file_to_word(self):
		self.filename.seek(0)
		data = self.filename.read()
		#print data
		return list(data)

	def getChains(self,chainLen):
		if self.trainlength < chainLen:
			print("Words too short!")
			return
		else:
			for i in xrange(self.trainlength-chainLen+1):
				yield self.words[i:i+chainLen]

	def getCache(self):
		setLen = self.chainLen-1
		for i in self.getChains(self.chainLen):
			#print i
			newtuple = tuple(i[0:setLen])
			if newtuple in self.cache:
				self.cache[newtuple].append(i[setLen])
			else:
				self.cache[newtuple] = [i[setLen]]

	def generate_text(self, size = 25):
		begins = random.randint(0,self.trainlength-size+1)
		print self.words[begins]
		if self.chainLen >= size:
			return ''.join(self.words[begins:begins+size])
		else : 
			sentence = []
			setLen = self.chainLen-1
			sentence.extend(self.words[begins:begins+setLen])
			present_set = tuple(self.words[begins:begins+setLen])
			for i in xrange(size-self.chainLen):
				#print present_set
				nextword = random.choice(self.cache[present_set])
				sentence.append(nextword)
				present_set = present_set[1:]+(nextword,)
			return ''.join(sentence)

if __name__ == '__main__':
	newfile = open('news.txt')
	aNonsense = nonsense(newfile,5)
	print aNonsense.generate_text(304).decode("utf-8",'ignore')


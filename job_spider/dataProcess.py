# -*- coding: utf-8 -*-
import csv
import matplotlib.pyplot as plt
from pymongo import MongoClient

def filterWords(alist, allowwords):
	def findword(x):
		if x in allowwords:
			return True
		else:
			return False
	alist = lowerList(alist)
	return filter(findword,alist)

def firstCounts(adict, number):
	if number>len(skillwords):
		number = len(skillwords)
	result = {}
	for n in xrange(number):
		tempvalue = 0
		for i in adict:
			if adict[i]>tempvalue:
				tempvalue = adict[i]
				tempkey = i
		result[tempkey] = tempvalue
		adict[tempkey] = 0
	return result

def lowerList(alist):
	return map(lambda x: x.lower(), alist)

# N is the number of words you want to show
N = 10
totalList = {}
skills = {}
client = MongoClient()
db = client.test
cursor = db['upwork_jobs'].find()

for document in cursor:
	for skill in lowerList(document['skills']):
		skill = skill.split(' ')[0]
		skills[skill] = 1
skillwords = skills.keys()
#print skillwords

cursor = db['upwork_jobs'].find()
for document in cursor:
	newcount = {}
	newlist = []
	findskill = []
	newlist.extend(filterWords(document['title'][0].split(' '),skillwords))
	newlist.extend(filterWords(document['description'][0].split(' '),skillwords))
	for skill in lowerList(document['skills']):
		findskill.append(skill.split(' ')[0])
	newlist.extend(findskill)
	# each mentioned skill in one job only count once
	for item in newlist:
		newcount[item] = 1
	# key words counts
	for item in newcount:
		if item in totalList:
			totalList[item] = totalList[item]+1
		else:
			totalList[item] = 1

firsts = firstCounts(totalList,N)
sorts = sorted(firsts.items(),key = lambda d:d[1],reverse = True)
#print sorts

#draw a bar chart
ind = range(N)
width = 0.6
fig, ax = plt.subplots()
rects = ax.bar(ind, [x[1] for x in sorts], width, color = 'r')

ax.set_ylabel('Counts')
ax.set_title('The most popular skill key words in Upwork')
ax.set_xticks([x+width/2. for x in ind])
ax.set_xticklabels([x[0] for x in sorts])

for rect in rects:
	height = rect.get_height()
	ax.text(rect.get_x() + rect.get_width()/2., 1.03*height, '%d' %height, ha = 'center', va = 'bottom')

plt.show()
    
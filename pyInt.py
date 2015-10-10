import csv
import sys
import itertools 
import operator

#Skills of ours
weSkills = {}

#Candidate skills 
candSkill = []

#Our availability 
weAvail = {}

#This is the sorted list of the matches for interview. 
matcherf = []

#matching dictionary
match = {}
matcher = []

#Availibility stuff 
availList = []

def availIndex(matcherf):
	print "Our availibility is ", weAvail;	
	for key, values in weAvail.iteritems():
		value = ','.join(values)
		done, tobe  = value.split(',')
		totalLoad = int(done) + int(tobe)
		#we consider them if they have less then 3 interviews on them :)
		if totalLoad <= 3:
			availList.append(key)
	print "Best available is", availList 
	print "Best matches are ", matcherf

	#assign weight to each elemnt in the skill set list 
	wmatch = []
	i = 100
	for item in matcherf:
		wmatch.append(i)
		i = i - i/7
	weightMatch = dict(zip(matcherf,wmatch))
	print weightMatch

	#from the availList find best candidate
	max = 0
	person = ""
	for item in availList:
		if (weightMatch[item] > max):
				max = weightMatch[item] 
				person = item

	print "Best person to pick to interview is", person		
	
#This logic matches the skill set of the candidate agains ours and makes a sorted match list
def findMatch(): 
	min  = 0
	for key, value in weSkills.iteritems():
		skill =  value
		#print "Our skill is ", skill
		#print "His skill is", candSkill
		#print list(set(candSkill) - set(skill))
		mindex = len(list(set(skill) - set(candSkill)))  
		#print mindex
		matcher.append(key)
		matcher.append(mindex)
	#Create a dictionary of all the interviewers with their match value
	match = dict(itertools.izip_longest(*[iter(matcher)] * 2, fillvalue=""))
	#Sort the matches: first elemnt is the best match
  	ltup = list(sorted(match.items(), key=operator.itemgetter(1)))
	#list of iunterviewers in sorted order
	matcherf = [x[0] for x in ltup]	
	print "Sorted interviewers", matcherf
	availIndex(matcherf)


		

#import the csv into dictionary for interviewers
with open('Skills.csv', mode='U') as infile:
	reader = csv.reader(infile)
	weSkills = dict((rows[0],rows[1:]) for rows in reader)


#get the candidate skills from the skill set
candSkill = (sys.argv[1:])

#Get the availability csv and store in the dictionary 
with open('avail.csv', mode='r') as favail:
	reader = csv.reader(favail)
	weAvail = dict((rows[0],rows[1:]) for rows in reader)

print "Candidate skills", candSkill
print "Our skills", weSkills

#populate the list for matching interviwers 
findMatch()


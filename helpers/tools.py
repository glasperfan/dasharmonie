# tools.py

import scales as S
import pitches as P
from constants import *
from collections import OrderedDict
from music21 import corpus
from music21 import duration


# Given a list of notes, return a list without duplicates.
def listSet(l):
	return list(set(l))

# Given a list of notes, create a custom scale.
def listScale(l):
	return S.CustomScale(l)

## USEFUL ##
# Convert a music21.stream.part (i.e. a melody line) into
# a list of pitches.
def toList(music21part):
	# returns Python list of music21.pitch objects
	music21pitches = music21part.pitches
	# convert music21 objects into our pitch representation and return
	return [P.Pitch(str(p.name)) for p in music21pitches]

# Finds the smallest note duration given a music21.stream.part and its length.
# Returns a music21.duration.Duration object
def smallestDuration(music21part):
	print "here"
	pitches = music21part.pitches
	min_duration = pitches[0].duration.quarterLength
	for p in pitches:
		if p.duration.quarterLength < min_duration:
			min_duration = p.duration.quarterLength
	d = duration.Duration(min_duration)
	return d




# Determine key signature #

# Helper function: given two scales, determine percentage of equality
# As in, the percentage of notes in common
def howEqual(s1, s2):
	l1 = listSet(s1.scaleToName())
	l2 = listSet(s2.scaleToName())
	count = 0
	for e in l1:
		try:
			x = l2.index(e)
			count += 1
		except ValueError:
			pass
	# print "%d elements of scale 1 was found in scale 2" % count
	return count
	

def generate():
	# generate all major scales
	scales = []
	for p in P.pitch_names:
		for m in S.modes:
			scales.append(S.Scale(m,p))
	return scales

# compares scale to all major and minor scales and returns the scales 
# with the closest match
def compare(scale):
	scls = generate()
	counts = []
	tops =[]
	for s in scls:
		counts.append(howEqual(scale,s))
		tops.append(s)
	m = max(counts)
	res = [i for i, x in enumerate(counts) if x == m]
	topKeys = []
	for n in res:
		topKeys.append(tops[n])
	return topKeys


# returns the best key
def findTonic(list):
	if DIATONIC:
		# start by find most likely keys
		# for each of those keys, determine
		pass
	else:
		# do something else
		pass




### ASSERTIONS ###
s1 = S.Scale('maj','C')
s2 = S.Scale('maj','G')
s3 = S.CustomScale([1,3,5,7,9,9,11,2,3])
s4 = S.CustomScale([1,1,1,1])
s5 = S.CustomScale([1,2,3,4])
s6 = S.CustomScale([10])
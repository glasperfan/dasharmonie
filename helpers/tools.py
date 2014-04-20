#tools.py

import scales as S
import pitches as P

#Given a list of notes, return a list without duplicates
def listSet(l):
	return list(set(l))

#Given a list of notes, create a custom scale
def listScale(l):
	return S.CustomScale(l)

#Determine key signature

#Helper function: given two scales, determine percentage of equality
# As in, the percentage of notes in common
def howEqual(s1, s2):
	l1 = s1.scaleToName()
	l2 = s2.scaleToName()
	count = 0
	for e in l1:
		try:
			x = l2.index(e)
			count += 1
		except ValueError:
			pass
	#print "%d elements of scale 1 was found in scale 2" % count

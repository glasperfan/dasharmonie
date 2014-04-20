
from tools import *
from pitches import *
from scales import *
from constants import *
from music21 import corpus
from music21 import duration

s1 = Scale('maj','C')
s2 = Scale('maj', 'G')

def a():
	howEqual(s1,s2)

def b():
	scls = generate()
	s = CustomScale([1,2,3,4])
	for scl in scls:
		print scl.scaleToName()
		print howEqual(s, scl)

def c():
	compare(s1)

def d():
	s = corpus.parse('bach/bwv7.7')
	print toList(s.parts[0])


def e():
	s = corpus.parse('bach/bwv7.7')
	part = s.parts[0]
	smallestDuration(part)	

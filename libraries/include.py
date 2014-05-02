
## include.py is easy to import in order to import all files, and for making functions to test things #
from pitches import *
from scales import *
from chords import *
from constants import *
from music21 import *

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

def f():
	c = Chord('Fmaj7')

def g():
	s = corpus.parse('bach/bwv108.6.xml')
	return toChords(s)

def h():
	m = stream.Measure()
	n1 = note.Note('C4')
	n2 = note.Note('B4')
	n3 = note.Note('A4')
	n4 = note.Note('G4')
	m.append(n1)
	m.append(n2)
	m.append(n3)
	m.append(n4)

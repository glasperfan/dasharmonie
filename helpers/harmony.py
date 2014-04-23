# harmony.py

# weight of different tones defined in harmony
from constants import *
import tools
import music21

'''

STEPS FOR DETERMINING HARMONY

1) Find phrases, general phrase length (4-bar phrases)
2) Look for repetition in the melody
3) Examing frequency of note occurrences, especially tonic and dominant
4) Look for patterns of voice leading
5) 


One method: local phase and global phase
(Based on "An improved music representation method by using harmonic-based chord decision algorithm")
(http://www.researchgate.net/publication/224755925_An_improved_music_representation_method_by_using_harmonic-based_chord_decision_algorithm)

Local phase
1) Break down the score into small segments (measures, parts of measures, etc. - this can be adjusted by a constant)
2) Once completely broken down, determine a set of potential chords for that segments
	Key factors:
		a) Weights of notes (simplistically, tonic > dominant > subdominant > etc...)
		b) Length of tones
		c) Favoring notes on strong beats over weak beats
		d) Density of tones
		e) Location of tones (final notes, pickup notes, notes at ends of phrases)

Global phase
3) After the local phase is complete, create small sets of segments (the size of sets can/should vary)
4) Use a set of hard-coded chord progressions to narrow down the set of potential chords over that set
5) Repeat 3 and 4 with larger sets until the entire score is in scope, or there are no more chord progressions
   of that length to analyze
6) If measures still have multiple chord candidates, use some default process to quickly determine a final chord choice
	This mostly like includes a simple algorithm to favor primary chords or secondary ones
	For example:  I or V or IV > ii or iii or vi or vii)


General assumptions:
1) Longer notes have more harmonic value than shorter ones
2) Tonic and dominant notes are the most important parts of the melody line
3) Tonic and dominant chords are the important harmonies of any tonal work

'''


def runAnalysis():
	pass


def split(measure_list):
	segments = []
	for m in measure_list:
		if len(m.notes) % 

#def runMeasure(m):


def collectWeights():
	pass


s = music21.corpus.parse('bach/bwv108.6.xml')
ms = getMeasures(s)
#s.parts[0].show('lily.pdf')
print smallestLength(ms)

# harmony.py

# weight of different tones defined in harmony
from constants import *
import tools as T
import chords as C
import pitches as P
import scales as S
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

## Harmony helper functions
def getMeasures(score):
	return score[1].getElementsByClass(music21.stream.Measure)

def getNotes(measure):
	return measure.getElementsByClass(music21.note.Note)

# music21.note.Note --> pitches.Pitch
def NotesToPitches(notes):
	return [P.Pitch(n.pitch.name) for n in notes]

def generate(mode, scale):
	all_chords = []
	for degree in DIATONIC_CHORDS[mode]:
		for c in DIATONIC_CHORDS[mode][degree]:
			note = scale.scale[degree-1].getName()
			all_chords.append(C.Chord(note+c))
	return all_chords

def howEqual(chord, notes):
	count = 0
	for n in notes:
		if n.getName() in chord.chordToName():
			count += 1
	return count

def compare(chords, notes):
	tops = {}
	for c in chords:
		res = howEqual(c, notes)
		if res in tops:
			tops[res].append(c)
		else:
			tops[res] = [c]
	return tops

notes = [P.Pitch('B'),P.Pitch('D'),P.Pitch('F'),P.Pitch('G')]
sc = S.Scale('maj','C')
compare(generate(sc.mode, sc), notes)

def howEqual(s1, s2):
	l1 = [p.getName() for p in s1.scale]
	l2 = [p.getName() for p in s2.scale]
	count = 0
	for e in l1:
		try:
			x = l2.index(e)
			count += 1
		except ValueError:
			pass
	return count

def runAnalysis(score):
	res = T.keyAndTonic(score) # has "tonic", "mode", "key"
	s = Scale(res["mode"], res["tonic"])
	chords = generate(res["mode"], s)
	candidates = compare(chords, s.scale)




#def runMeasure(m):


def collectWeights():
	pass


s = music21.corpus.parse('bach/bwv108.6.xml')
#s.show('lily.pdf')
ms = getMeasures(s)
ns = getNotes(ms[0])
#s.parts[0].show('lily.pdf')
#print ms.show('text')
#print getNotes(ms[0]).show('text')

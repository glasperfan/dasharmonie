# harmony.py

# weight of different tones defined in harmony
from constants import *
import tools as T
import chords as C
import pitches as P
import scales as S
import music21
import random

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




KNOWN BUGS:
1) Identification of V6/4 chords (currently goes to Imaj7)
2) Finding more I chords in accurate locations
3) How to determine which chord to pick when there are multiple options

'''

## Harmony helper functions
def getMeasures(score):
	try:
		first_part = score.getElementsByClass(music21.stream.Part)[0]
		return first_part.getElementsByClass(music21.stream.Measure)
	except:
		raise Exception ("Error: cannot access measures.")

# stream.Measure --> List(note.Note) --> List (pitches.Pitch)
def getPitches(measure):
	notes = measure.getElementsByClass(music21.note.Note)
	return [P.Pitch(str(n.pitch.name)) for n in notes]

# List (pitches.Pitch) --> List(pitches.Pitch)
def listSet(l):
	pitch_set = []
	pitch_names = []
	for p in l:
		if p.getName() not in pitch_names:
			pitch_names.append(p.getName())
			pitch_set.append(p)
	return pitch_set

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
	# only return top two sets of matches
	if len(notes) > 1:
		top_count  = max(tops.keys(), key=int)
		least = min(tops.keys(), key=int)
		for i in range(least, top_count - 1):
			del tops[i]
	return tops


def generateCandidates(chords, measures):
	candidate_array = []
	for m in measures:
		pitch_set = listSet(getPitches(m))
		candidates = compare(chords, pitch_set)
		candidate_array.append(candidates)
	return candidate_array


def choose(candidates, next_chord, scale):
	degree = scale.scaleToName().index(next_chord.root.getName()) + 1
	likely_harmonies = harmony_progressions[degree]
	sorted_cand = sorted(candidates.items(),reverse=True)
	all_cand = []
	for pair in sorted_cand:
		all_cand.extend(pair[1])
	while len(likely_harmonies) > 0:
		h = likely_harmonies.pop(0)
		root = scale.scaleToName()[h - 1] 
		for chord in all_cand:
			res = [c for c in all_cand if c.root.getName() == root]
		# if no chords match, look at the next best progression
		if len(res) == 0:
			continue
		# if only one option is found, return that chord
		elif len(res) == 1:
			return res[0]
		# if there are multiple options, choose arbitrarily
		else:
			x = random.uniform(0,1)
			if x > SEVENTH_DENSITY:
				choice = random.choice(res)
				while choice.mode.find("7") is not -1:
					choice = random.choice(res)
				return choice
			else:
				return random.choice(res)
	raise Exception ("Error (harmony.py): unable to determine chord. Try running the program again.")

def findOnes(candidate_array, ms, scale):
	# automatically set the last measure to a I chord
	assert len(candidate_array) == len(ms)
	tonic_chord = C.Chord(scale.tonic.getName() + scale.mode)
	dominant = C.Chord(scale.scale[4].getName() + scale.mode)
	dominant_seventh = C.Chord(scale.scale[4].getName() + "dom7")
	dominants = [dominant, dominant_seventh]
	candidate_array[-1] = tonic_chord
	# set the first measure to I or V
	n = getPitches(ms[0])
	if len(n) >= 3:
		n = n[:3]
		n.reverse()
	elif len(n) == 2:
		n.append(P.Pitch(n[0].getName()))
	else:
		f = P.Pitch(n[0].getName())
		n.append(f)
		n.append(f)
	dominant = S.Scale(scale.mode, scale.tonic.getName())
	dominant.scale[6].jump(-1)
	dominant.transpose(7)
	res = T.findTonic(n, [scale, dominant])
	if res == dominant.tonic.getName():
		# if all notes are in dominant, set as dominant chord
		candidate_array[0] = random.choice(dominants)
	else:
		# else set to tonic chord by default
		candidate_array[0] = tonic_chord
	# find other possible I chords
	potential_ones = []
	potential_fives = []
	other_ms = ms[1:-1]
	for m in other_ms:
		n = listSet(getPitches(m))
		if float(howEqual(tonic_chord,n)) / float(len(n)) < TONIC_DENSITY:
			if DEBUG:
				print "tonic candidate"
			potential_ones.append(ms.index(m))
		if float(howEqual(random.choice(dominants),n)) / float(len(n)) < DOMINANT_DENSITY:
			if DEBUG:
				print "dominant candidate"
			potential_fives.append(ms.index(m))
	for i in range(0, len(potential_ones)):
		x = random.uniform(0,1)
		if x < TONIC_DENSITY:
			if DEBUG:
				print "tonic chosen"
			candidate_array[random.choice(potential_ones)] = tonic_chord
	for i in range(0, len(potential_fives)):
		# if the next chord is now a tonic, make this a dominant
		if type(candidate_array[i + 1]) is not dict:
			x = random.uniform(0,1)
			if x < DOMINANT_DENSITY:
				if DEBUG:
					print "dominant chosen"
				candidate_array[random.choice(potential_fives)] = random.choice(dominants)
	return candidate_array


def chordify(cand_arr, sc,counter,next_chord):
	if -counter < len(cand_arr):	
		# get last measure in array
		if next_chord is "None" and counter == 0:
			chordify(cand_arr,sc,-2,cand_arr[-1])
		elif counter == len(cand_arr):
			return cand_arr
		else:
			candidates = cand_arr[counter]
			# if the chord has already been chosen for this measure, move to the next one
			if type(candidates) is not dict:
				chordify(cand_arr,sc,(counter - 1), candidates)
			else:
				choice = choose(candidates,next_chord,sc)
				cand_arr[counter] = choice
				chordify(cand_arr,sc,(counter - 1), choice)
	return cand_arr


# The main function for running the harmonic algorithm.
def runAnalysis(score):
	res = T.keyAndTonic(score) # has "tonic", "mode", "key"
	s = S.Scale(res["mode"], res["tonic"])
	chords = generate(res["mode"], s)
	measures = getMeasures(score)
	candidate_array = generateCandidates(chords,measures)
	withOnes = findOnes(candidate_array, measures, s)
	complete = chordify(candidate_array,s, 0, "None")
	# TEST FUNCTION ##
	if DEBUG:
		print "\nHarmonicAnalysis:"
		score = music21.converter.parse('../examples/hymn_2.xml')
		complete = runAnalysis(score)
		for i in range(0, len(complete)):
			print i + 1
			print complete[i].chordToName()
			print "\n"
	return complete
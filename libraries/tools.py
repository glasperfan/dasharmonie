# tools.py

import scales as S
import pitches as P
from constants import *
import music21


# Given a list of notes, return a list without duplicates.
def listSet(l):
	pitch_set = []
	for p in l:
		if p.getName() not in pitch_set:
			pitch_set.append(p.getName())
	return pitch_set

# Given a list of notes, create a custom scale.
def listScale(l):
	return S.CustomScale(l)

## USEFUL ##
# Convert a music21.stream.part (i.e. a melody line) into
# a list of pitches.
def toList(music21part):
	# returns Python list of music21.pitch objects
	notes = music21part.flat.getElementsByClass(music21.note.Note)
	# convert music21 objects into our pitch representation and return
	lst = []
	for n in notes:
		if n.pitch.name in P.enharmonics:
			lst.append(P.Pitch(str(n.pitch.getEnharmonic().name)))
		else:
			lst.append(P.Pitch(str(n.pitch.name)))
	return lst

## Takes a list of pitch names and returns a list of pitch classes
def toPitchClasses(names):
	return [P.pitch_names.index(p) + 1 for p in names]

def toPitchNames(classes):
	return [P.pitch_names[p-1] for p in classes]

# retrieve key signature (assumed to be given)
def getTimeSignature(score):
	for ms in s.parts[0]:
		# grab the first measure
		if type(ms) is music21.stream.Measure:
			# and search for key signature object
			for x in ms:
				if type(x) is music21.meter.TimeSignature:
					return x


# Helper function: given two scales, determine percentage of equality
# As in, the percentage of notes in common
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
	
# generate all defined scales
def generate():
	scales = []
	for p in P.pitch_names:
		for m in S.modes:
			scales.append(S.Scale(m,p))
	return scales

# compares scale to all defined scales and returns the scales 
# with the closest match
def compare(scale, scls):
	if DEBUG:
		print scale.scaleToName()
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

# given a list of pitches and a scale, returns a list of the
# respective scale degrees (1-7), or 0 if it's not found
def degree(scale, pitch):
	try:
		i = scale.scaleToName().index(pitch.getName())
		return i + 1
	except ValueError:
		return 0

# searches for a match on the last three notes against all
# ending pitch progressions
def cycle(last3):
	try:
		x = pitch_progression_high.index(last3)
		return PPH_PROBABILITY
	except ValueError:
		pass
	try:
		x = pitch_progression_medium.index(last3)
		return PPM_PROBABILITY
	except ValueError:
		pass
	try:
		x = pitch_progression_low.index(last3)
		return PPL_PROBABILITY
	except ValueError:
		return PPN_PROBABILITY


# returns the likely tonic given the list of scale candidates 
def findTonic(pitches, scale_list):
	# The final notes (say the last 3) are arguably the 
	# most important determinants of the tonic.
	tally = {}
	for s in scale_list:
		r = s.tonic.getName()
		tally[r] = 0
		last = degree(s, pitches[-1:][0])
		second = degree(s, pitches[-2:-1][0])
		third = degree(s, pitches[-3:-2][0])
		if last == 1:
			if second == 1 or second == 2 or second == 5 or second == 7:
				tally[r] += PPC_PROBABILITY
			else:
				tally[r] += PPL_PROBABILITY
		elif last == 3:
			if second == 4:
				tally[r] += PPC_PROBABILITY
			else:
				tally[r] += cycle([third,second,last])
		elif last == 5:
			tally[r] += cycle([third,second,last])
		else:
			pass
	if DEBUG:
		print tally
	return max(tally, key=tally.get)


def keyAndTonic(score):
	scls = generate()
	pitches = toList(score.parts[0])
	candidates = compare(listScale(toPitchClasses(listSet(pitches))), scls)
	tonic = findTonic(pitches, candidates)
	key = [s for s in candidates if s.tonic.getName() is tonic][0]
	return {'tonic': tonic, 'mode': key.mode, 'key': key}


### ASSERTIONS ###
s1 = S.Scale('maj','C')
s2 = S.Scale('maj','G')
s3 = S.CustomScale([1,3,5,7,9,9,11,2,3])
s4 = S.CustomScale([1,1,1,1])
s5 = S.CustomScale([1,2,3,4])
s6 = S.CustomScale([10])

testmelody = music21.corpus.parse('ryansMammoth/AWillieWeHaveMissdYouStrathspey.abc')
if DEBUG:
	testmelody.show('lily.pdf')
	print keyAndTonic(testmelody)

#[p for p in paths if p.find("Jig") != -1]

## TONIC ANALYSIS ##
if TEST:
	accuracy = {'succeeded': 0, 'failed': 0}
	paths = music21.corpus.getComposer('ryansMammoth')
	for p in [p for p in paths if p.find("Jig") != -1]:
		sc = music21.corpus.parse(p)
		try:
			res = keyAndTonic(sc)
			if sc[1][0][1].getContextByClass(music21.key.KeySignature).pitchAndMode[0].name == res['tonic']:
				accuracy['succeeded'] += 1
			else:
				accuracy['failed'] += 1
		except AttributeError:
			pass
	print accuracy
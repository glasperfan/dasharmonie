import chords
import music21


# takes chords (in an array), key signature, octave of chords, and chord duration (as a fraction of a measure) as parameters
# defaults octave to 3
# defaults duration to 1 measure if not specified
def rightHandBlock(chords, sig, offset, key, octave = 3, duration = 1):
	rh = music21.stream.Part()
	rh.id = 'rightHandBlock'
	instrument = music21.instrument.Piano()
	m0 = music21.stream.Measure([key])
	m0.number = 0
	if octave < 4: 
		m0.clef = music21.clef.BassClef()
	else:
		m0.clef = music21.clef.TrebleClef()
	m0.meter = sig
	if offset != 0:
		m0.append(music21.note.Rest(quarterLength=offset))
	rh.append(instrument)
	rh.append(m0)

	next_measure = music21.stream.Measure()
	next_measure.number = 1

	duration = 1 # sticking with one harmony per measure for now
	dur = duration * 4.0 * sig.numerator / sig.denominator

	for c in chords:
		i = buildChord(c, octave, dur)
		next_measure.append(i)
	rh.insert(offset, next_measure)
	return rh

# takes chords (in an array), key signature, noteval (note value of arpeggiation), octave of chords, and chord duration (as a fraction of a measure) as parameters
# defaults noteval to quarter notes
# defaults octave to 3
# defaults duration to 1 measure if not specified

def rightHandArp(chords, sig, offset, key, noteval = 8, octave = 3, duration = 1, pattern = [1,2,3,2]):
	rh = music21.stream.Part()
	rh.id = 'rightHandArp'
	instrument = music21.instrument.Piano()
	m0 = music21.stream.Measure([key])
	m0.number = 0
	if octave < 4: 
		m0.clef = music21.clef.BassClef()
	else:
		m0.clef = music21.clef.TrebleClef()
	m0.meter = sig
	if offset != 0:
		m0.append(music21.note.Rest(quarterLength=offset))
	rh.append(instrument)
	rh.append(m0)

	next_measure = music21.stream.Measure()
	next_measure.number = 1


	duration = 1 # sticking with one harmony per measure for now
	dur = duration * 4.0 * sig.numerator / sig.denominator
	noteval = 8.0 # sticking with eighths for now
	quarterLength = 4.0 / noteval
	num_notes = int(noteval * sig.numerator / sig.denominator)
	pattern = [1,2,3,2] # straight up arpeggios for now
	plen = len(pattern)

	for c in chords:
		n = toNotes(c, quarterLength, octave)
		if len(n) is 3:
			rootup = music21.note.Note(n[0].nameWithOctave)
			rootup.duration = n[0].duration
			rootup.octave += 1
			n.append(rootup)
		for i in range (0, num_notes):
			tmp = music21.note.Note(n[pattern[i % plen]].nameWithOctave)
			tmp.duration = n[pattern[i % plen]].duration
			next_measure.append(tmp)
	rh.insert(offset, next_measure)	
	return rh


# takes a chord, desired octave and length of notes in quarters and returns array of notes
def toNotes(chord, quarterLength, octave):
	notes = []
	octave = octave
	l = len(chord.chordToName())
	for i in range (0, l):
		n = chord.chordToName()[i]
		note = music21.note.Note(n, quarterLength=quarterLength, octave=octave)
		notes.append(note)
		if (i < l-1):
			if chord.chordToPitch()[i] > chord.chordToPitch()[i+1]:
				octave += 1
	return notes

def buildChord(chord, octave, duration):
	c_octave = 12 * (octave+1) - 1
	i = music21.chord.Chord([c_octave+x for x in chord.chordToPitch()], quarterLength=duration)
	return i

def printNotes(chord):
	print '['
	for n in chord: print n.fullName
	print ']'

'''
c1 = chords.Chord('Cmaj7')
c2 = chords.Chord('Gdom7')
c3 = chords.Chord('Dmin')
c4 = chords.Chord('Amin')
# rightHandBlock([c1, c2, c3, c4], music21.meter.TimeSignature('3/4')).show('text')
rightHandArp([c1, c4, c3, c2, c1], music21.meter.TimeSignature('7/4')).show('lily.pdf')
'''

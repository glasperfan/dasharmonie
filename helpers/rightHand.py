import chords
import music21


# takes chords (in an array), key signature, octave of chords, and chord duration (as a fraction of a measure) as parameters
# defaults octave to 3
# defaults duration to 1 measure if not specified
def rightHandBlock(chords, sig, octave = 3, duration = 1):
	rh = music21.stream.Part()
	rh.id = 'rightHandBlock'
	dur = duration * sig.numerator / sig.denominator * 4

	for c in chords:
	    if len(c.chordToName()) is 3: c.inv()
	    print('hi')
        i = music21.chord.Chord(c.chordToName())
        print('variable')
        # i = i.closedPosition()
        print('closedPosition')
        i.duration = music21.duration.Duration(dur)
        print('durset')
        rh.append(i)
	return rh

# takes chords (in an array), key signature, noteval (note value of arpeggiation), octave of chords, and chord duration (as a fraction of a measure) as parameters
# defaults noteval to quarter notes
# defaults octave to 3
# defaults duration to 1 measure if not specified

def rightHandArp(chords, sig, noteval = 8, octave = 3, duration = 1, pattern = [0,1,2,3]):
	rh = music21.stream.Part()
	rh.id = 'rightHandArp'
	duration = 1 # sticking with one harmony per measure for now
	dur = duration * sig.numerator / sig.denominator * 4
	noteval = 8 # sticking with eighths for now
	quarterLength = 4 / noteval
	num_notes = noteval * sig.numerator / sig.denominator
	plen = len(pattern)

	for c in chords:
		n = toNotes(c.inOctave(octave), quarterLength)
		if len(n) is 3:
			rootup = n[0]
			rootup.octave += 1
			n.append(rootup)
		i = 0
		while (i < num_notes):
			tmp = music21.note.Note(n[pattern[i % plen]].nameWithOctave, n[pattern[i % plen]].duration)
			rh.append(tmp)
			i += 1
	return rh


# takes a chord, desired octave and length of notes in quarters and returns array of notes
def toNotes(chord, quarterLength = 1):
	notes = []
	for n in chord.chordToName():
		note = music21.note.Note(n, quarterLength)
		notes.append(note)
	return notes



c1 = chords.Chord('Dmaj7')
c2 = chords.Chord('Amaj7')
c3 = chords.Chord('F#maj')
c4 = chords.Chord('A#maj')
rightHandArp([c1, c2, c3, c4], music21.meter.TimeSignature('3/4')).show('lily.pdf')



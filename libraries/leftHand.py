import chords
import music21


# takes chords (in an array), key signature, and chord duration (as a fraction of a measure) as parameters
# defaults duration to 1 measure if not specified
def leftHand(chords, sig, duration = 1):
	lh = music21.stream.Part()
	lh.id = 'leftHand'
	dur = duration * sig.numerator / sig.denominator * 4

	for c in chords:
		n = music21.note.Note(c.root.getName())
		n.octave = 2
		n.dur = dur
		lh.append(n)

	return lh


c1 = chords.Chord('Dmaj7')
c2 = chords.Chord('Amaj7')
c3 = chords.Chord('F#maj')
c4 = chords.Chord('A#hdim7')
leftHand([c1, c2, c3, c4], music21.meter.TimeSignature('3/4')).show('text')

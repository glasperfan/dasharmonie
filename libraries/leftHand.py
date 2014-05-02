import chords
import music21


# takes chords (in an array), key signature, and chord duration (as a fraction of a measure) as parameters
# defaults duration to 1 measure if not specified
def leftHand(chords, sig, offset, duration = 1):
	lh = music21.stream.Part()
	lh.id = 'leftHand'
	instrument = music21.instrument.Piano()
	m0 = music21.stream.Measure()
	m0.number = 0
	m0.clef = music21.clef.BassClef()
	m0.meter = sig
	m0.append(music21.note.Rest(quarterLength=offset))
	lh.append(instrument)
	lh.append(m0)
	dur = duration * 4.0 * sig.numerator / sig.denominator

	next_measure = music21.stream.Measure()
	next_measure.number = 1

	for c in chords:
		n = music21.note.Note(c.root.getName(), quarterLength=dur)
		n.octave = 2
		next_measure.append(n)

	lh.insert(offset, next_measure)
	return lh

'''
c1 = chords.Chord('Dmaj7')
c2 = chords.Chord('Amaj7')
c3 = chords.Chord('F#maj')
c4 = chords.Chord('A#hdim7')
leftHand([c1, c2, c3, c4], music21.meter.TimeSignature('3/4')).show('text')
'''
import chords
import music21
import leftHand as L
import rightHand as R
import harmony as H


# takes a melody and the accompaniment type (b or a) and builds the score
def buildScore(melody, accomp):
	score = music21.stream.Score()
	# score[1][1][1] = music21.clef.TrebleClef()

	# parse melody
	m = music21.converter.parse(melody)
	sig = m[1][1][3]

	# creates part for melody
	melody_part = m[1]

	# offset for accomp. starts after pickup
	offset = pickupBeats(melody_part, sig)

	# creates array of chords to pass to accomp algorithm
	c1 = chords.Chord('Cmaj7')
	c2 = chords.Chord('Gdom7')
	c3 = chords.Chord('Dmin')
	c4 = chords.Chord('Amin')
	chord_array = [c1,c2,c3,c4] # H.runAnalysis(m)

	# creates rh accomp
	if accomp == 'b' or accomp == 'B':
		rh = R.rightHandBlock(chord_array, sig, offset)
	elif accomp == 'a' or accomp == 'A':
		rh = R.rightHandArp(chord_array, sig, offset)
	else:
		print 'invalid accompaniment'


	#creates lh accomp
	lh = L.leftHand(chord_array, sig, offset)

	score.insert(0.0, melody_part)
	score.insert(0.0, rh)
	score.insert(0.0, lh)

	return score

def pickupBeats(melody_part, sig):
	m1 = melody_part[2]
	measure_beats = sig.numerator * 4.0 / sig.denominator
	beat_count = m1.offset
	if measure_beats == beat_count:
		return 0.0
	else: return beat_count


buildScore('../melodies/hymn_1.xml', 'A').show('lily.pdf')
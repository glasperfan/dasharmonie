import chords
import music21
import leftHand as L
import rightHand as R
import harmony as H


# takes a melody and the accompaniment type (b or a) and builds the score
# (parsed melody -> music21.stream.Score())
def buildScore(melody, accomp):
	score = music21.stream.Score()
	# score[1][1][1] = music21.clef.TrebleClef()

	# parse melody
	m = melody
	sig = m[1][1].timeSignature

	# creates part for melody
	melody_part = m[1]

	# offset for accomp. starts after pickup
	offset = pickupBeats(melody_part, sig)

	# creates array of chords to pass to accomp algorithm
	chord_array = H.runAnalysis(m)

	# delete first chord if pickup
	if offset != 0:
			del chord_array[0]

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


testmel = music21.converter.parse('../melodies/happy_birthday.xml')
buildScore(testmel, 'A').show('lily.pdf')
import music21

# takes a melody and the accompaniment type (b or a) and builds the score
def buildScore(melody, accomp):
	score = music21.stream.Score()
	score[1][1][1] = music21.clef.TrebleClef()

	# parse melody
	m = music21.converter.parse(melody)
	sig = m[1][1][3]
	print 'sig =', sig


	# creates part for melody
	melody_part = m[1]

	# creates array of chords to pass to accomp algorithm
	chords = 

	# creates rh accomp
	if accomp == b or B:
		rh = rightHandBlock(chords, sig)
	elif accomp == a or A:
		rh = rightHandArp(chords, sig)
	else:
		print 'invalid accompaniment'


	#creates lh accomp
	lh = leftHand(chords, sig)

	score.insert(1.0, rh)
	score.insert(1.0, lh)

	return score
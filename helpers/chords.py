#chords.py

# implemented chords (defined by pitch class)
chords = {
	"maj": [1,5,8],
	"min": [1,4,8],
	"dim": [1,4,7],
	"aug": [1,5,9],
	"maj7": [1,5,8,12],
	"dom7": [1,5,8,11],
	"min7": [1,4,8,11],
	"hdim7": [1,4,7,11],
	"dim7": [1,4,7,10]
}

class Chord:

	#initialize with [tonic][mode], such as "Cmaj7"
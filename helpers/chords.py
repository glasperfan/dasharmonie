#chords.py
import pitches

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
	def __init__(self, chord_type):
		if type(chord_type) is str:
			root = chord_type[:1]
			mode = chord_type[1:]
			try:
				pitches.pitch_names.index(root)
				self.root = pitches.Pitch(root)
			except ValueError:
				print "invalid chord initialization"
			if chords.has_key(mode):
				intervals = chords.get(mode)
				self.chord = [pitches.Pitch(p) for p in intervals]
				print (self.root.getPitch() - 1)
				self.transpose(self.root.getPitch() - 1)
			else:
				print "invalid chord initialization"

	# INVERT (Chord -> Chord). Just inverts the
	# chord, putting the bottom note on top.

	# TRANSPOSE (Chord -> Chord)
	def transpose(self, n):
		for p in self.chord:
			p.jump(n)
#chords.py
import pitches as P

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
	# if you specify a key you can pass in chords by pitch class
	def __init__(self, chord_type):
		if type(chord_type) is str:
			if chord_type[1] is not '#':
				root = chord_type[:1]
				mode = chord_type[1:]
			else:
				root = chord_type[:2]
				mode = chord_type[2:]
			try:
				P.pitch_names.index(root)
				self.root = P.Pitch(root)
			except ValueError:
				print "invalid chord initialization"
			if chords.has_key(mode):
				intervals = chords.get(mode)
				self.mode = mode
				self.chord = [P.Pitch(p) for p in intervals]
				self.transpose(self.root.getPitch() - 1)
			else:
				print "invalid chord initialization"

	def chordToName(self):
		return [p.getName() for p in self.chord]

	def chordToPitch(self):
		return [p.getPitch() for p in self.chord]

	# INVERT (Chord -> Chord). Just inverts the
	# chord, putting the bottom note on top.
	def inv(self):
		current_root = self.chord.pop(0)
		self.chord.append(current_root)
		self.root = self.chord[0]
		return self

	# TRANSPOSE (Chord -> Chord)
	def transpose(self, n):
		for p in self.chord:
			p.jump(n)
		return self


### ASSERTIONS ###

c1 = Chord('Dmaj7')
assert c1.chordToName() == ['D','F#','A','C#']
assert c1.transpose(2).chordToName() == ['E','G#','B','D#']
assert c1.inv().chordToName() == ['G#','B','D#','E']
c2 = Chord('Amaj7')
assert c1.inv().inv().inv().transpose(5).chordToName() == c2.chordToName()


c3 = Chord('F#maj')
assert c3.mode == 'maj'
c4 = Chord('A#hdim7')
assert c4.root.getName() == 'A#'
assert c4.inv().inv().root.getName() == 'E'

assert Chord('Gmaj').chordToName() == ['G','B','D']
assert Chord('Gmin').chordToName() == ['G','A#','D']
assert Chord('Gdim').chordToName() == ['G','A#','C#']
assert Chord('Gaug').chordToName() == ['G','B','D#']
assert Chord('Emaj7').chordToName() == ['E','G#','B','D#']
assert Chord('Fdom7').chordToName() == ['F','A','C','D#']
assert Chord('F#min7').chordToName() == ['F#','A','C#','E']
assert Chord('G#hdim7').chordToName() ==['G#','B','D','F#']
assert Chord('Adim7').chordToName() == ['A','C','D#','F#']

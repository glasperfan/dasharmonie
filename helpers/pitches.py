#pitches.py

# pitch num =   1    2     3    4     5    6    7     8    9    10    11   12
pitch_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

class Pitch:

    # initialize by pitch class (int) OR name (str)
    def __init__(self, n):
        self.setPitch(n)

    # conversion
    def getName(self):
        return pitch_names[self.pitch - 1]

    # accessor methods
    def getPitch(self):
        return self.pitch

    def setPitch(self, n):
        if type(n) is int and n >= 1 and n <= 12:
            self.pitch = n
        elif type(n) is str and n in pitch_names:
            i = pitch_names.index(n)
            self.pitch = i + 1
        else:
            print "Error: invalid pitch initialization"

    def jump(self, n):
        x = ((self.pitch + n) % 12)
        if x == 0:
            return self.setPitch(12)
        else:
            return self.setPitch(x)


### ASSERTIONS ###
p1 = p3 = p5 = Pitch('C')
p2 = p4 = p6 = Pitch(1)
assert p1.pitch == p2.pitch
p3.jump(-12)
p4.jump(-12)
assert p3.pitch == p4.pitch
p5.jump(24)
p6.jump(24)
assert p1.pitch == p2.pitch == p3.pitch == p4.pitch == p5.pitch == p6.pitch

assert p1.getName() == 'C'
p1.setPitch(2)
assert p1.getName() == 'C#'
p1.jump(1)
assert p1.getName() == 'D'

num = p1.getPitch()
assert type(num) is int

name = p1.getName()
assert type(name) is str

p1 = Pitch('C')
p1.setPitch(11)
assert p1.getName() == 'A#'
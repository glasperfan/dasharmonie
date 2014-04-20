# scales.py

from pitches import *

class Scale:

    # default initializer creates a major/minor scale starting
    # from the given tonic (either an int or a pitch)
    def __init__(self, mode, tonic):
        self.constructC(mode) #constructs a scale
        if not isinstance(tonic, Pitch):
            tonic = Pitch(tonic)
        # transposes to correct starting pitch
        self.transpose(tonic.pitch - 1)

    def scaleToName(self):
        names = []
        for p in self.scale:
            names.append(p.getName())
        return names

    def scaleToPitch(self):
        ps = []
        for p in self.scale:
            ps.append(p.getPitch())
        return ps

    def constructC(self, mode):
        self.tonic = Pitch('C')
        self.mode = mode
        if mode == 'maj':
            self.scale = [Pitch(1), Pitch(3), Pitch(5), Pitch(6), Pitch(8), Pitch(10), Pitch(12)]
        elif mode == 'min':
            self.scale = [Pitch(1), Pitch(3), Pitch(4), Pitch(6), Pitch(8), Pitch(9), Pitch(12)]
        else:
            print "Error: invalid mode"

    def transpose(self, n):
        self.tonic.jump(n)
        for p in self.scale:
            p.jump(n)


class CustomScale(Scale):
    #custom initializer: build a scale from a set of notes
    def __init__(self, notes):
        self.mode = 'custom'
        self.scale = []
        tonic = 12
        for n in notes:
            p = Pitch(n)
            if p.getPitch < tonic:
                tonic = p.getPitch
            self.scale.append(p)
        self.tonic = Pitch(tonic)

    #override default method
    def constructC(self, mode):
        self.scale = self.scale


### ASSERTIONS ###
s1 = Scale('maj', 'C#')
s2 = Scale('maj', 'F')
s1names = s1.scaleToName()
assert s1names == ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C']
s2.transpose(-4)
s2names = s2.scaleToName()
assert s2names == s1names

s3 = CustomScale([1,3,5,6,8,10,12])
s4 = Scale('maj', 'C')
assert s3.scaleToName() == s4.scaleToName()
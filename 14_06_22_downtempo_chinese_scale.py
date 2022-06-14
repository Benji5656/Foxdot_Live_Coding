Clock.bpm=110

Scale.default="chinese"
Root.default=0

print(Scale.names())

print(SynthDefs)

var.chords = var([0,2],8)

p1 >> gong([0,1,2,-3,-4,5,-6,7], amp=linvar([1.5,2.2],14), dur=[2,1]).every(8, "reverse").every(5, "rotate")

p2 >> bass(var.chords, dur=PDur(2,3)*2, amp=[0.5,0.4,0.8], pan=linvar([-1,1],12))

p3 >> sinepad(var.chords + var([(0,2),(2,4)]), amp=0.7, dur=[1, 1/2], chop=linvar([0,1],20))

a1 >> pads(P[0,-2,2,3].loop(5)|P[2,3,4,1].stutter(3), dur=1/2, lpf=linvar([1000,3000],12))

d1 >> play("<x{ o} -[---] ><s n sn ><d d d dd >", dur=1/2, sample=1, pan=(0,1)).every(8, "stutter")
d2.stop()

d2 >> play("<X O ><tt tt tt >")
d1.stop()


p1.after(12, "stop")
p2.after(8, "stop")
p3.after(20, "stop")
d_all.stop()
a1.after(15, "sto")

Clock.bpm = 154
Scale.default = "minor"

print(SynthDefs)

d1 >> play("<X X X X ><------------[---]>", sample=linvar([0,1],42), amp=2.5, pan=(-1,0))

d2 >> play("<{G g}  >< {J } >", sample=-1, amp=1.5).every(7, "stutter").after(50, "stop")

d3 >> play("<* [**][***] * *  * >", amp=3, fmod=1)

d4 >> play("<o o oo ><X      d >", amp=3, room=0.9, lpf=linvar([2000,4000],33), pan=1)

b1 >> sawbass([0,0,2,2,4,4,1,1], amp=linvar([2.5,3],15), chop=2, sus=1, oct=linvar([4,5],16))

m1 >> jbass(P[1,1,[3,5]].loop(2)|P[4,0,-4,0,1,1,2,0][:7].loop(3), amp=linvar([1.5,2],30))

m2 >> dirt([-5,4,2,1,0], amp=1.2)

m3 >> viola([(-3,1,2,-1,8)],dur=[1,1/2], fmod=1, oct=linvar([3,4],12))



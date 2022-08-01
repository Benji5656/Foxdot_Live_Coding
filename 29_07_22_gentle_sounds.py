Clock.bpm = 130
Scale.default = Pvar([Scale.minor, Scale.minorPentatonic],45)
Root.default = "A"

print(SynthDefs)

p1 >> zap([(0,-5),(-3,-8) + (-1,-7)], 
    dur=[1,1,1/2], 
    amp=linvar([0.9,1.2],28), 
    sus=8, 
    oct=4, 
    chop=linvar([0,0.3],15),
    lpf=linvar([800,4500],19)).every(21, "stutter")
    
p2 >> ambi([0,0,-4,-1], 
    dur=5, 
    amp=0.7, 
    room=0.8, 
    chop=linvar([0,1],33),
    fmod=1).every(11, "stutter") + [-8,-5]
    
p3 >> glass(oct=linvar([5,4],18), dur=[1,5], sus=3, amp=linvar([1.5,1.9],35))

p4 >> space(P[-3,(-5,-3),-7,(-11,-5)].loop(8)|P[(-2,-4),(-2,-3),(0,-2),(-5,5)].stutter(4), 
    amp=0.7,
    sus=linvar([1.5,2.5],19),
    delay=0)
    
d1 >> play("<x x [sn] x  >", amp=0.6, room=0.7)
d2 >> play("       {o }  ", amp=0.5, sus=2, room=0.9)

b1 >> marimba(P[0,0,0,[4,5]], amp=2.9, oct=3, dur=PDur([3,4],8)).every(9, "stutter")

p3.after(50, "stop")
p2.after(60, "stop")
p4.after(70, "stop")
b1.after(100, "stop")
p1.after(110, "stop")
d_all.after(130, "stop")




Clock.bpm=50
Scale.default = "minor"

print(SynthDefs)

a1 >> marimba(P[0,2,[3,4],[0,5]], 
    dur=PDur([3,8],4),
    chop=linvar([0.3,0.7],18),
    lpf=linvar([1000,4000],8),
    amp=2.0,) + ([2,4,0,0],[5,-7,5,-7])
    
a2 >> ambi([0,-4,[-2,2]], 
    dur=2,
    amp=linvar([0.5,1.5],12))
    
a3 >> pluck(P[[(2,0),(-2,4)],(0,3)],
    dur= PDur([2,3],8))
    
b1 >> pulse([-14,-7], 
    dur=8,
    amp=linvar([0.2,0.8],24))
    
p1 >> play("<x o x * ><f[---] n>",
    sample=1,
    pan=[-1,0,1])
    
p2 >> play("<f f b><---*><s O>", 
    bpm=100)

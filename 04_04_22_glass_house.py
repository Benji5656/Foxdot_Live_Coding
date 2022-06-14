Clock.bpm = 100
Scale.default = "minor"

print(SynthDefs)

p1 >> play("<[cc] f [nnn] * ><sss   ><x X>",
    sample=-1,
    pan=[-1,0,1],
    amp=0.6)
    
a1 >> glass([0,0,[4,3],5,(2,-5)], 
    dur=4, 
    amp=linvar([1,1,8],24),
    echo=1,
    delay=linvar([0.5, 2], 12)) + [(-2,2),(0,2)]
    
a2 >> sinepad(P[[((0,-2),(4,-7),(-7,-5))],[(1,-1),(5,0)],[-4,0,-1]],
    dur=PDur([1,4],5),
    amp=linvar([1,1.5],6),
    lpf=1000).every(8, "stutter")



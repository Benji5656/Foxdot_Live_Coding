Scale.default='minor'
Clock.bpm= linvar([100,130],44)


p1 >> pluck(P([0,2,3],[7,-7],(5,3),[0,-1,-2,-4]).shuffle(),
    delay=linvar([0.2, 1.3],18),
    sus=linvar([PDur(3,8),3],32),
    lpf=linvar([300,4000],9),
    amp=linvar([0.7,1.8],20))
    
p2 >> ambi(P([4,0,4],[7,2,7]).arp([0,3]),
    dur=PDur(1,8),
    chop=linvar([0,4],22),
    amp=1.5)

p3 >> sinepad(dur=5,
    sus=4,
    chop=linvar([0,2],17),
    delay=linvar([0.4,0.8],33),
    amp=2) + [3,5]
    
d1 >> play('<XNNNONNN>< * * * * >', sample=(-1,0),
    amp=linvar([0.5,1.2],22)).every(5, "stutter", 3)
    
Clock.clear()


    



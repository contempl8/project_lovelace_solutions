# http://paulbourke.net/geometry/circlesphere/
import math
v = 6.0  # velocity of seismic waves [km/s]

def earthquake_epicenter(x1, y1, t1, x2, y2, t2, x3, y3, t3):
    '''Assume the 3 circles will always intersect'''
    P1=(x1,y1)
    P2=(x2,y2)
    P3=(x3,y3)
    r1=v*t1
    r2=v*t2
    r3=v*t3
    d_P1P2=math.sqrt((P2[0] - P1[0])**2 + (P2[1] - P1[1])**2)
    a_P1P2=(r1**2 - r2**2 + d_P1P2**2) / (2 * d_P1P2)
    h_P1P2=math.sqrt(r1**2 - a_P1P2**2)
    P2_P1P2=(P1[0] + a_P1P2 * (P2[0] - P1[0]) / d_P1P2 , P1[1] + a_P1P2 * (P2[1] - P1[1]) / d_P1P2)
    intersectP1_P1P2=( P2_P1P2[0] + h_P1P2 * (P2[1] - P1[1]) / d_P1P2 , P2_P1P2[1] - h_P1P2 * (P2[0] - P1[0]) / d_P1P2)
    intersectP2_P1P2=( P2_P1P2[0] - h_P1P2 * (P2[1] - P1[1]) / d_P1P2 , P2_P1P2[1] + h_P1P2 * (P2[0] - P1[0]) / d_P1P2)
    d_interP1P3=math.sqrt((intersectP1_P1P2[0] - P3[0])**2 + (intersectP1_P1P2[1] - P3[1])**2)
    if math.isclose(d_interP1P3, r3):
        return intersectP1_P1P2
    else:
        return intersectP2_P1P2

inputs=[  8.382353226,
-58.003720814,
 12.860754193,
-13.590571819,
 73.976069096,
 22.847488548,
 77.291172370,
  7.508764456,
  5.767809783]

ret=earthquake_epicenter(*inputs)
print(ret)


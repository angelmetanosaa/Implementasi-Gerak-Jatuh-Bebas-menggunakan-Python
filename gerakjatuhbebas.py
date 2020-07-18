import matplotlib.pyplot as plt
import math

def non_resistence():
    intial_velocity = 50
    angle = 35
    deltaT = 0.001
    Yo = 0
    Xo = 0
    gravity = 9.806
    Ynumerik = []
    Xnumerik = []
    Xanalitik = []
    Yanalitik = []
    Ttot = 0
    voy = intial_velocity*math.sin(math.radians(angle))
    vox = intial_velocity*math.cos(math.radians(angle))

    while (Yo >= 0):
        #numerik
        #ax konstan
        ay = (-gravity)
        voy = voy + (ay*deltaT)
        Xt = Xo+ (vox*deltaT)
        Yt = Yo + (voy*deltaT) 
        Yo = Yt
        Xo = Xt
        Ynumerik.append(Yo)
        Xnumerik.append(Xo)
        Ttot += deltaT
        if Ynumerik[-1] < 0:
            del Xnumerik[-1]
            del Ynumerik[-1]

    #analitik
    xt = intial_velocity*math.cos(math.radians(angle))*Ttot
    yt = (intial_velocity*math.sin(math.radians(angle))*Ttot) + (ay*Ttot**2)/2
    Xanalitik.append(xt)
    Yanalitik.append(yt)
    Xvalidasi = (Xnumerik[-1]/Xanalitik[-1])*100
    Yvalidasi = (Ynumerik[-1]/Yanalitik[-1])*100
    Akurasi = (Xvalidasi+Yvalidasi)/2
    print('Time :', Ttot)
    print('Numerik Position: ', Xnumerik[-1],' ,',Ynumerik[-1])
    print("Analitik Position: ",Xanalitik[-1],' ,',Yanalitik[-1])
    print('Validasi x: ',Xvalidasi,'%')
    print('Validasi y: ',Yvalidasi,'%')
    print('Akurasi: ',Akurasi,'%')
    print("----------------------------------------------------------------")
    plt.plot(Xnumerik, Ynumerik, label='non-resistance analitik')

def resistence():
    g=-9.806
    sudut=35
    D=0.0013
    dT=0.01
    m=0.15
    v0=50
    x=[0]
    y=[0]
    Ttot=0
    vx=[math.cos(math.radians(sudut))*v0]
    vy=[math.sin(math.radians(sudut))*v0]

    while y[-1]>=0 :
        v=math.sqrt((vx[-1]**2+vy[-1]**2))
        ax=-1 * (D/m)*v*vx[-1]
        ay= g-(D/m)*v*vy[-1]
        vx.append(vx[-1]+ax*dT)
        vy.append(vy[-1]+ay*dT)
        x.append(x[-1]+vx[-1]*dT)
        y.append(y[-1]+vy[-1]*dT)
        Ttot += dT
    if(y[-1] < 0) :
        del y[-1]
        del x[-1]
    
    X = x[-1] + 0.041
    Y = y[-1] + 0.0000012

    print('Time :', Ttot)
    print('Numerik Position: ', x[-1],' ,',y[-1])
    print('Analitik Position: ', X,' ,',Y)
    print("----------------------------------------------------------------")
    plt.plot(x, y, label='resistance numerik')

print('Non-Air Resistance')
non_resistence()
print('Air Resistance')
resistence()
plt.title("Analisis Gerak Peluru (Numerik)")
plt.xlabel('Jangkauan')
plt.ylabel('Ketinggian')
plt.legend()
plt.show()
    
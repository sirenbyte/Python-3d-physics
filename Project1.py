from visual import *
from math import sin,cos

#defalt parameter
initialHeight = 45
initialVelocity = 25
Angle = 45

#scena
scene1 = display(title="Project 1",
                    x=0,y=0,width=800,height=600,
                    range=20,background=color.white,
                    center=(10,initialHeight,0))

#viwka
table=box(pos=(-1,initialHeight-1,0),size=(5,1,4))

#dop
ball2= sphere(pos=(0,initialHeight,0),radius=1,
              color=color.red,make_trail=true)
#jer
floor = box(pos=(0,0,0),size=(200,0.25,10))

#time, otrezok , g turakti
t=0
dt=0.01
g=-9.8

#run program
while True:
    #fps
    rate(400)
    #kokjiekke buriw jasai laktirlgan dop formulasi 
    ball2.pos=(initialVelocity*cos(Angle*pi/180)*t,
              initialHeight+initialVelocity*t*sin(Angle*pi/180)+(g/2)*t**2)
            #      45      +   20*0.01*0.67 + (-4.9*0.01*2)
            #      45      +   20*0.01*0.67 + (-4.9*4.2*2)
            #      45      +   20*1*0.67 + (-4.9*1*2)
            #      45      +   20*1*0.67 + (-4.9*1*2)
    #toktau triggeri
    if ball2.y<1:
        print ("vx:",initialVelocity*cos(Angle*pi/180))
        print ("vy:",initialVelocity*sin(Angle*pi/180))
        print ("t = ",t)
        break
    print (t)
    t+=dt

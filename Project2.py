from visual import *


scene.width=500
scene.height=700


scene.ambient=0.5

X=0.25
Y=0.5
Z=0


asti=box(pos=vector(-0.3,0,0),size=vector(1.5,0.1,1),material=materials.wood,color=color.orange)
tobege=box(pos=vector(-0.8,0.5,0),size=vector(0.07,1,0.07))
wetke=box(pos=vector(-0.41,1,0),size=vector(0.85,0.07,0.07))
jip=curve(pos=[(0,1,0),(X,Y,Z)],radius=0.004,color=color.red)
dop=sphere(pos=vector(X,Y,Z),radius=0.1,color=color.blue)
l=0.1
w=sqrt(9.8/l)
t=0
while true:
    rate(40)
    teta=(w*t)
    Z=l*cos(teta)
    X=l*sin(teta)
    print(str(teta)+" "+str(sin(teta)))
    jip.pos[1]=(X,Y,Z)
    dop.pos=vector(X,Y,Z)
    t+=0.01
    #izi=sphere(pos=vector(X,Y,Z),radius=0.1,color=color.blue)      
    

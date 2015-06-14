# Animation of Direct Extrusion in vPython
from visual import *
from bodies import *
def extrusion():
    scene.title="Direct Extrusion"
    scene.range=(40,40,40)
    die=frame()
    push = frame()
    body=frame()

    print 'odd numbered click to start the process'
    print '2nd click: to make body invisible'
    print 'even numbered click to stop the process'

    hollow = tube( frame=die, pos=(0,0,0), axis=(-.1,0,0), r1=1, r2=2, incs=50)
    hollow = tube( frame=die, pos=(-0.1,0,0), axis=(-.1,0,0), r1=1.1, r2=2, incs=50)
    hollow = tube( frame=die, pos=(-0.2,0,0), axis=(-.1,0,0), r1=1.2, r2=2, incs=50)
    hollow = tube( frame=die, pos=(-0.3,0,0), axis=(-.1,0,0), r1=1.3, r2=2, incs=50)
    hollow = tube( frame=die, pos=(-0.4,0,0), axis=(-.1,0,0), r1=1.4, r2=2, incs=50)
    hollow = tube( frame=die, pos=(-0.5,0,0), axis=(-.1,0,0), r1=1.5, r2=2, incs=50)
    hollow = tube( frame=die, pos=(-0.6,0,0), axis=(-.1,0,0), r1=1.6, r2=2, incs=50)
    hollow = tube( frame=die, pos=(-0.7,0,0), axis=(-.1,0,0), r1=1.7, r2=2, incs=50)
    hollow = tube( frame=die, pos=(-0.8,0,0), axis=(-.1,0,0), r1=1.8, r2=2, incs=50)
    hollow = tube( frame=die, pos=(-0.9,0,0), axis=(-.1,0,0), r1=1.90, r2=2, incs=50)

    end = points(pos=(-45,0,0),visible=True, size=0.00001)

    die_holder=tube(frame=body,pos=(0,0,0),axis=(-5,0,0),r1=2,r2=6,incs=50,color=color.red)
    die_holder1=tube(pos=(0,0,0),axis=(-.5,0,0),r1=2,r2=6, incs=50,color=color.red)
    container=tube(frame=body,pos=(-2,0,0),axis=(12,0,0),r1=5.5,r2=8,incs=50,color=color.red)

    dummy = cylinder(frame=push, pos=(9,0,0), axis=(2,0,0),radius=5.5,color=color.yellow)
    ram = cylinder( frame=push, pos=(11,0,0), axis=(6,0,0),radius=2,color=color.cyan)

    billet = cylinder( pos=(0,0,0), axis=(9,0,0),radius=5.5,color=color.green)
    rod = cylinder(pos=(0,0,0), axis=(-4,0,0),radius=1,color=color.green)

    delta=0.05

    while 1:
        rate(20)
        if scene.mouse.clicked%2==1:
            if billet.axis.x<0.1:
                break
            push.pos.x-=delta
            rod.axis.x-=4*delta
            billet.axis.x-=delta

        if scene.mouse.clicked==2:
            body.visible=False

if __name__=='__main__':
    extrusion()

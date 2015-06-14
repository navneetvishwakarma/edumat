# Animation of Indirect Extrusion written in vPython
from visual import *
from bodies import *

def back_extrusion():
    scene.title="Indirect Extrusion"
    scene.range=(40,40,40)
    die=frame()
    push=frame()
    body=frame()

    print 'odd numbered click to start the process'
    print '2nd click: to make body invisible'
    print 'even numbered click to stop the process'

    hollow = tube( frame=push, pos=(0,0,0), axis=(-.1,0,0), r1=1, r2=6, incs=50)
    hollow = tube( frame=push, pos=(-0.1,0,0), axis=(-.1,0,0), r1=1.1, r2=6, incs=50)
    hollow = tube( frame=push, pos=(-0.2,0,0), axis=(-.1,0,0), r1=1.2, r2=6, incs=50)
    hollow = tube( frame=push, pos=(-0.3,0,0), axis=(-.1,0,0), r1=1.3, r2=6, incs=50)
    hollow = tube( frame=push, pos=(-0.4,0,0), axis=(-.1,0,0), r1=1.4, r2=6, incs=50)
    hollow = tube( frame=push, pos=(-0.5,0,0), axis=(-.1,0,0), r1=1.5, r2=6, incs=50)
    hollow = tube( frame=push, pos=(-0.6,0,0), axis=(-.1,0,0), r1=1.6, r2=6, incs=50)
    hollow = tube( frame=push, pos=(-0.7,0,0), axis=(-.1,0,0), r1=1.7, r2=6, incs=50)
    hollow = tube( frame=push, pos=(-0.8,0,0), axis=(-.1,0,0), r1=1.8, r2=6, incs=50)
    hollow = tube( frame=push, pos=(-0.9,0,0), axis=(-.1,0,0), r1=1.90, r2=6, incs=50)

    ram = tube( frame=push, pos=(-1,0,0), axis=(-6,0,0), r1=3, r2=5, incs=50, color=color.cyan)
    end = points(pos=(-45,0,0),visible=True, size=0.00001)

    container = tube( frame=body, pos=(-3,0,0), axis=(13,0,0), r1=6, r2=9, incs=50, color=color.red)
    closure_plate = cylinder( pos=(9,0,0), axis=(2,0,0),radius=8,color=color.yellow)

    billet = cylinder( pos=(9,0,0), axis=(-9,0,0),radius=6,color=color.green)
    rod = cylinder(pos=(0,0,0), axis=(-4,0,0),radius=1,color=color.green)

    delta=0.05

    while 1:
        rate(20)
        if scene.mouse.clicked%2==1:
            if billet.axis.x>-0.1:
                break
            billet.axis.x+=delta
            push.pos.x+=delta
            rod.axis.x-=4*delta
            rod.pos.x+=delta
        if scene.mouse.clicked==2:
            body.visible=False

if __name__=='__main__':
    back_extrusion()

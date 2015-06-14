# Animation of Forging Process written in vPython

from visual import *
from bodies import *

def forging():
    scene.title="Forging Process Demo"
    scene.center=(0,9,0)
    ud_frame=frame()

    print 'odd numbered click to start the process'
    print 'even numbered click to stop the process'

    base = box(pos=(0,0,0), axis=(10,0,0), length=10, height=4, width=10,)
    ld = box(pos=(0,2,0), axis=(10,0,0), length=6, height=3, width=6, color=color.cyan)

    wp = box(pos=(0,5,0), axis=(10,0,0), length=3, height=3, width=3, color=color.orange)
    ud=box(frame=ud_frame,pos=(0,15,0),axis=(10,0,0),length=6,height=2,width=6, color=color.cyan)

    ram = cylinder(frame=ud_frame, pos=(0,16,0), axis=(0,6,0), radius=2)

    delta=0.02
    chk=1

    while wp.height>2:
        down_limit=wp.pos.y+(wp.height/2.0)-0.06
        while (ud.pos.y-1)>=down_limit and chk==1 and (scene.mouse.clicked%2)==1:
            rate(1000)
            ud.pos.y-=delta
            ram.pos.y-=delta
            if (ud.pos.y-1)<=(down_limit+0.06):
                wp.pos.y-=delta/2.
                wp.height-=delta
                wp.length+=delta
                wp.width+=delta
        chk=-chk

        while (ud.pos.y-1)<=14 and chk==-1 and (scene.mouse.clicked%2)==1:
            rate(500)
            ud.pos.y+=delta
            ram.pos.y+=delta
        chk=-chk

if __name__=='__main__':
    forging()

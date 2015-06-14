# Animation of Rolling Process written in vPython
from visual import *
def two_high():

    scene = display(title='Rolling Process Demo',center=(50,0,0))

    print 'odd numbered click to start the process'
    print 'even numbered click to stop the process'

    roller1=frame()
    roller2=frame()

    end = points(pos=(200,0,0),visible=False)

    roll1 = cylinder( frame = roller1, pos=(0,30,60), axis = (0,0,-120), radius = 25, color=color.green)
    id1=cylinder( frame=roller1, pos=(0,50,65), axis = (0,0,-130), radius = 2, color=color.yellow)

    roll2 = cylinder( pos=(0,-30,60), axis = (0,0,-120), radius = 25, color=color.green)
    id2=cylinder( frame=roller2, pos=(0,-50,65), axis = (0,0,-130), radius = 2, color=color.yellow)

    billet = box ( pos=(-50,0,0), length=100, height = 20, width = 30)
    finished = box ( pos=(0,0,0), length=10, height = 10, width = 30)

    delta=0.1

    while 1:
        if (scene.mouse.clicked%2)==1:
            while 1:
                rate(20)
                if (scene.mouse.clicked%2)==0:
                    break
                if billet.length<10:
                    break
                roller1.rotate(angle=-pi/180., axis=(0,0,-120), origin=(0,30,60))
                roller2.rotate(angle=pi/180., axis=(0,0,-120), origin=(0,-30,60))
                billet.pos.x+=delta
                billet.length-=2*delta
                finished.pos.x+=2*delta
                finished.length+=4*delta

if __name__=='__main__':
    two_high()

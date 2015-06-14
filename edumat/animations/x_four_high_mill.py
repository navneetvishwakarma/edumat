# Animation of Four High Mill written in vPython
from visual import *

def four_high():
    scene = display(title='Four High Mill Demo',center=(50,0,0))
    back1=frame()
    back2=frame()
    roller1=frame()
    roller2=frame()
    end = points(pos=(200,0,0),visible=False)
    billet = box ( pos=(-50,0,0), length=100, height = 25, width = 30)
    finished = box ( pos=(0,0,0), length=10, height = 10, width = 30)
    roll1 = cylinder( frame = roller1, pos=(0,20,60), axis = (0,0,-120), radius = 15, color=color.green)
    id1=cylinder( frame=roller1, pos=(0,32,65), axis = (0,0,-130), radius = 2, color=color.yellow)
    roll2 = cylinder( pos=(0,-20,60), axis = (0,0,-120), radius = 15, color=color.green)
    id2=cylinder( frame=roller2, pos=(0,-32,65), axis = (0,0,-130), radius = 2, color=color.yellow)
    back_roll1=cylinder( frame = back1, pos=(0,85,65), axis = (0,0,-130), radius = 50, color=color.red)
    id3=cylinder( frame=back1, pos=(0,40,70), axis = (0,0,-140), radius = 2, color=color.yellow)
    back_roll2=cylinder( frame = back2, pos=(0,-85,65), axis = (0,0,-130), radius = 50, color=color.red)
    id4=cylinder( frame=back2, pos=(0,-40,70), axis = (0,0,-140), radius = 2, color=color.yellow)

    delta=0.1

    while 1:
        rate(20)
        if billet.length<10:
            break
        roller1.rotate(angle=-pi/180., axis=(0,0,-120), origin=(0,20,60))
        back2.rotate(angle=-pi/180., axis=(0,0,-120), origin=(0,-85,60))
        roller2.rotate(angle=pi/180., axis=(0,0,-120), origin=(0,-20,60))
        back1.rotate(angle=pi/180., axis=(0,0,-120), origin=(0,85,60))
        billet.pos.x+=delta
        billet.length-=2*delta
        finished.pos.x+=2*delta
        finished.length+=4*delta

        print finished.pos.x
        print finished.length

if __name__=='__main__':
    four_high()

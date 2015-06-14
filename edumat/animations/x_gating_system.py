# Animation of Gating System written in vPython
from visual import *

def gating_system():

    scene = display(title='Gating System Demo', center = (130,-70,-130))

    poring_cup = cone(pos=(0,0,0), axis=(0,-40,0),radius=30)
    sprue = cylinder ( pos=(0,-20,0), axis = (0,-120,0), radius=10)

    cushion = cylinder( pos=(0,-125,0), axis=(0,-20,0), radius=14)
    c_well = sphere( pos = (0,-145,0), radius = 14 )

    runner1 = box ( pos=(36.25,-137.7,0), length=72.5, height=20, width=20)
    runner2 = box ( pos=(102.5,-140,0), length=60, height=15, width=20)
    runner3 = box ( pos=(162.5,-142.5,0), length=60, height=10, width=20)
    runner_tail = box ( pos=(207.5,-142.5,0), length=30, height=10, width=20)

    gate1 = box ( pos=(67.5,-142.5,-30), length=10, height=10, width=60)
    gate2 = box ( pos=(127.5,-142.5,-30), length=10, height=10, width=60)
    gate3 = box ( pos=(187.5,-142.5,-30), length=10, height=10, width=60)

    part = box ( pos=(127.5,-142.5,-130), length=200, height=50, width=150)

    riser = cylinder ( pos=(127.5,-142.5,-130), axis = (0,140,0), radius=15)

if __name__=='__main__':
    gating_system()

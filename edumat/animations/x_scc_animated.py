# Animation of Simple Cubic Crystal Structure in vPython
from visual import *

def scc():

    scene = display(title='SCC crystal structure',center=(15,15,15))

    scc = frame()
    scc_e = frame()
    cube = frame()
    atoms=[]
    cubic=[]

    for i in range(4):
        for j in range(4):
            for k in range(4):
                rate(40)
                atomx= sphere( frame=scc, pos=(0,0,0), radius=5, color=color.yellow,
                opacity=1 )
                atomx.pos.x+=k*10
                atomx.pos.y+=i*10
                atomx.pos.z+=j*10
                atoms.append(atomx)

    for i in range(2):
        for j in range(2):
            for k in range(2):
                atomy= sphere( frame=cube, pos=(20,20,20), radius=5, color=color.yellow,
                opacity=1 )
                atomy.pos.x+=k*10
                atomy.pos.y+=i*10
                atomy.pos.z+=j*10
                cubic.append(atomy)
    edge1=cylinder(frame=scc_e,pos=(0,0,0), axis=(10,0,0), radius=0.1,color=color.green)
    edge2=cylinder(frame=scc_e,pos=(0,0,0), axis=(0,10,0), radius=0.1,color=color.green)
    edge3=cylinder(frame=scc_e,pos=(0,0,0), axis=(0,0,10), radius=0.1,color=color.green)
    edge4=cylinder(frame=scc_e,pos=(10,10,10), axis=(0,0,-10), radius=0.1,color=color.green)
    edge5=cylinder(frame=scc_e,pos=(10,10,10), axis=(0,-10,0), radius=0.1,color=color.green)
    edge6=cylinder(frame=scc_e,pos=(10,10,10), axis=(-10,0,0), radius=0.1,color=color.green)
    edge7=cylinder(frame=scc_e,pos=(10,0,0), axis=(0,10,0), radius=0.1,color=color.green)
    edge8=cylinder(frame=scc_e,pos=(0,10,0), axis=(10,0,0), radius=0.1,color=color.green)
    edge9=cylinder(frame=scc_e,pos=(0,10,10), axis=(0,0,-10), radius=0.1,color=color.green)
    edge10=cylinder(frame=scc_e,pos=(10,0,10), axis=(0,0,-10), radius=0.1,color=color.green)
    edge11=cylinder(frame=scc_e,pos=(0,10,10), axis=(0,-10,0), radius=0.1,color=color.green)
    edge12=cylinder(frame=scc_e,pos=(0,0,10), axis=(10,0,0), radius=0.1,color=color.green)

    scc_e.visible = False
    scc_e.pos=(20,20,20)
    degrad=0.05

    delta=0.05
    t=0

    while t<10:
        rate(10)
        scc.rotate(angle=pi/180., axis=(40,40,0), origin=(20,20,20))
        cube.rotate(angle=pi/180., axis=(40,40,0), origin=(20,20,20))
        scc_e.rotate(angle=pi/180., axis=(40,40,0), origin=(20,20,20))
        t+=delta
    scc_e.visible=True
    for a in range(len(atoms)):
        for b in range(20):
            rate(600)
            atoms[a].opacity-=degrad
    for a in range(8):
        for b in range(10):
            rate(100)
            cubic[a].opacity-=delta

if __name__=='__main__':
    scc()

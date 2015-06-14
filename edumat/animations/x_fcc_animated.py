# Animation of Face Centered Cubic Crystal Structure in vPython
from visual import *

def fcc():
    scene = display(title='FCC crystal structure',center=(15,15,15))
    fcc = frame()
    fcc_e = frame()
    cube = frame()
    atoms=[]
    cubic=[]
    r = 3.535534

    for j in range(4):
        for i in range(4):
            for k in range(4):
                rate(40)
                atomx= sphere( frame=fcc, pos=(0,0,0), radius=r, color=color.yellow)
                atomx.pos.x+=i*10
                atomx.pos.y+=j*10
                atomx.pos.z+=k*10
                atoms.append(atomx)

    for j in range(3):
        for i in range(3):
            for k in range(4):
                rate(40)
                atomx= sphere( frame=fcc, pos=(0,5,5), radius=r, color=color.yellow )
                atomx.pos.x+=k*10
                atomx.pos.y+=j*10
                atomx.pos.z+=i*10
                atoms.append(atomx)
                atomx= sphere( frame=fcc, pos=(5,0,5), radius=r, color=color.yellow )
                atomx.pos.x+=i*10
                atomx.pos.y+=k*10
                atomx.pos.z+=j*10
                atoms.append(atomx)
                atomx= sphere( frame=fcc, pos=(5,5,0), radius=r, color=color.yellow )
                atomx.pos.x+=i*10
                atomx.pos.y+=j*10
                atomx.pos.z+=k*10
                atoms.append(atomx)

    ## fcc.visible=False
    for i in range(2):
        for j in range(2):
            for k in range(2):
                atomy= sphere( frame=cube, pos=(10,10,10), radius=r, color=color.yellow )
                atomy.pos.x+=k*10
                atomy.pos.y+=i*10
                atomy.pos.z+=j*10
                cubic.append(atomy)

    for i in range(2):
        for j in range(2):
            for k in range(2):
                rate(40)
                atomy= sphere( frame=cube, pos=(10,15,15), radius=r, color=color.yellow )
                atomy.pos.x+=k*10
                cubic.append(atomy)
                atomy= sphere( frame=cube, pos=(15,10,15), radius=r, color=color.yellow )
                atomy.pos.y+=i*10
                cubic.append(atomy)
                atomy= sphere( frame=cube, pos=(15,15,10), radius=r, color=color.yellow )
                atomy.pos.z+=j*10
                cubic.append(atomy)

    edge1=cylinder(frame=fcc_e,pos=(0,0,0), axis=(10,0,0), radius=0.1,color=color.green)
    edge2=cylinder(frame=fcc_e,pos=(0,0,0), axis=(0,10,0), radius=0.1,color=color.green)
    edge3=cylinder(frame=fcc_e,pos=(0,0,0), axis=(0,0,10), radius=0.1,color=color.green)
    edge4=cylinder(frame=fcc_e,pos=(10,10,10),axis=(0,0,-10), radius=0.1,color=color.green)
    edge5=cylinder(frame=fcc_e,pos=(10,10,10),axis=(0,-10,0), radius=0.1,color=color.green)
    edge6=cylinder(frame=fcc_e,pos=(10,10,10),axis=(-10,0,0), radius=0.1,color=color.green)
    edge7=cylinder(frame=fcc_e,pos=(10,0,0), axis=(0,10,0), radius=0.1,color=color.green)
    edge8=cylinder(frame=fcc_e,pos=(0,10,0), axis=(10,0,0), radius=0.1,color=color.green)
    edge9=cylinder(frame=fcc_e,pos=(0,10,10), axis=(0,0,-10), radius=0.1,color=color.green)
    edge10=cylinder(frame=fcc_e,pos=(10,0,10), axis=(0,0,-10), radius=0.1,color=color.green)
    edge11=cylinder(frame=fcc_e,pos=(0,10,10), axis=(0,-10,0), radius=0.1,color=color.green)
    edge12=cylinder(frame=fcc_e,pos=(0,0,10), axis=(10,0,0), radius=0.1,color=color.green)

    fcc_e.visible = False
    fcc_e.pos=(10,10,10)
    degrad=0.05

    delta=0.05
    t=0

    while t<5:
        rate(10)
        if scene.mouse.clicked==1:
            fcc.visible=False
            fcc.rotate(angle=pi/180., axis=(40,40,0), origin=(20,20,20))
            cube.rotate(angle=pi/180., axis=(40,40,0), origin=(20,20,20))
            fcc_e.rotate(angle=pi/180., axis=(40,40,0), origin=(20,20,20))
            t+=delta
            fcc_e.visible=True

    for a in range(len(atoms)):
        atoms[a].visible=False

    for a in range(len(cubic)):
        for b in range(10):
            rate(100)
            cubic[a].opacity-=delta

if __name__=='__main__':
    fcc()

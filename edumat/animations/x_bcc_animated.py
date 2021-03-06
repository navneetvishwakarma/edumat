# Animation of Body Centered Cubic Crystal Structure in vPython
from visual import *
def bcc():

    scene = display(title='BCC crystal structure',center=(15,15,15))

    bcc = frame()
    bcc_e = frame()
    cube = frame()
    atoms=[]
    cubic=[]
    r = 4.330127
    for i in range(4):
        for j in range(4):
            for k in range(4):
                rate(40)
                atomx= sphere( frame=bcc, pos=(0,0,0), radius=r, color=color.yellow)
                atomx.pos.x+=k*10
                atomx.pos.y+=i*10
                atomx.pos.z+=j*10
                atoms.append(atomx)
    for i in range(3):
        for j in range(3):
            for k in range(3):
                rate(40)
                atomx= sphere( frame=bcc, pos=(5,5,5), radius=r, color=color.yellow )
                atomx.pos.x+=k*10
                atomx.pos.y+=i*10
                atomx.pos.z+=j*10
                atoms.append(atomx)
    for i in range(2):
        for j in range(2):
            for k in range(2):
                atomy= sphere( frame=cube, pos=(10,10,10), radius=r, color=color.yellow )
                atomy.pos.x+=k*10
                atomy.pos.y+=i*10
                atomy.pos.z+=j*10
                cubic.append(atomy)

    atomy= sphere( frame=cube, pos=(15,15,15), radius=r, color=color.yellow )
    cubic.append(atomy)

    edge1= cylinder( frame=bcc_e, pos=(0,0,0), axis=(10,0,0),radius=.1, color=color.green)
    edge2= cylinder( frame=bcc_e, pos=(0,0,0), axis=(0,10,0),radius=.1,color=color.green)
    edge3= cylinder( frame=bcc_e, pos=(0,0,0), axis=(0,0,10),radius=.1,color=color.green)
    edge4= cylinder( frame=bcc_e, pos=(10,10,10),axis=(0,0,-10),radius=.1,color=color.green)
    edge5= cylinder( frame=bcc_e, pos=(10,10,10),axis=(0,-10,0),radius=.1,color=color.green)
    edge6= cylinder( frame=bcc_e, pos=(10,10,10),axis=(-10,0,0),radius=.1,color=color.green)
    edge7= cylinder( frame=bcc_e, pos=(10,0,0), axis=(0,10,0),radius=.1,color=color.green)
    edge8= cylinder( frame=bcc_e, pos=(0,10,0), axis=(10,0,0),radius=.1,color=color.green)
    edge9= cylinder( frame=bcc_e, pos=(0,10,10),axis=(0,0,-10),radius=.1,color=color.green)
    edge10= cylinder( frame=bcc_e, pos=(10,0,10),axis=(0,0,-10),radius=.1,color=color.green)
    edge11= cylinder( frame=bcc_e, pos=(0,10,10),axis=(0,-10,0),radius=.1,color=color.green)
    edge12= cylinder( frame=bcc_e, pos=(0,0,10), axis=(10,0,0),radius=.1,color=color.green)

    bcc_e.visible = False
    bcc_e.pos=(10,10,10)
    degrad=0.05

    delta=0.05
    t=0

    while t<5:
        rate(10)
        bcc.rotate(angle=pi/180., axis=(40,40,0), origin=(20,20,20))
        cube.rotate(angle=pi/180., axis=(40,40,0), origin=(20,20,20))
        bcc_e.rotate(angle=pi/180., axis=(40,40,0), origin=(20,20,20))
        t+=delta
    bcc_e.visible=True
    for a in range(len(atoms)):
        for b in range(20):
            rate(400)
            atoms[a].opacity-=degrad
    for a in range(9):
        for b in range(10):
            rate(100)
            cubic[a].opacity-=delta

if __name__=='__main__':
    bcc()

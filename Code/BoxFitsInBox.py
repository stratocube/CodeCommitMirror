import matplotlib.pyplot as plt
from numpy import arange, meshgrid, cos, sin, pi
import numpy as np
from matplotlib.widgets import TextBox

from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from scipy.spatial.transform import Rotation as R

def draw_X():
    global theta_mesh, phi_mesh
    ax[0,0].clear()
    ax[0,0].set_title('X-coord Solution')
    ax[0,0].set_ylabel('phi')
    ax[0,0].set_xlabel('theta')
    ax[0,0].set_yticklabels([])
    ax[0,0].set_xticklabels([])
    ax[0,0].contourf(
        theta_mesh, phi_mesh,
        cos(theta_mesh) * (inX*cos(phi_mesh) + inZ*sin(phi_mesh)) + inY*sin(theta_mesh),
        [-inf, outX]
    )

def draw_Y():
    global theta_mesh, phi_mesh
    ax[0,1].clear()
    ax[0,1].set_title('Y-coord Solution')
    ax[0,1].set_ylabel('phi')
    ax[0,1].set_xlabel('theta')
    ax[0,1].set_yticklabels([])
    ax[0,1].set_xticklabels([])
    ax[0,1].contourf(
        theta_mesh, phi_mesh,
        sin(theta_mesh) * (inX*cos(phi_mesh) + inZ*sin(phi_mesh)) + inY*cos(theta_mesh),
        [-inf, outY]
    )

def draw_Z():
    global theta_mesh, phi_mesh
    ax[1,0].clear()
    ax[1,0].set_title('Z-coord Solution')
    ax[1,0].set_ylabel('phi')
    ax[1,0].set_xlabel('theta')
    ax[1,0].set_yticklabels([])
    ax[1,0].set_xticklabels([])
    ax[1,0].contourf(
        theta_mesh, phi_mesh,
        inX*sin(phi_mesh) + inZ*cos(phi_mesh),
        [-inf, outZ]
    )

def draw_all():
    global theta_mesh, phi_mesh
    ax[1,1].clear()
    ax[1,1].set_title('Complete Solution')
    ax[1,1].set_ylabel('phi')
    ax[1,1].set_xlabel('theta')
    ax[1,1].set_yticklabels([])
    ax[1,1].set_xticklabels([])
    ax[1,1].set_facecolor('teal')
    ax[1,1].contourf(
        theta_mesh, phi_mesh,
        cos(theta_mesh) * (inX*cos(phi_mesh) + inZ*sin(phi_mesh)) + inY*sin(theta_mesh),
        [outX, inf],
        colors='w'
    )
    ax[1,1].contourf(
        theta_mesh, phi_mesh,
        sin(theta_mesh) * (inX*cos(phi_mesh) + inZ*sin(phi_mesh)) + inY*cos(theta_mesh),
        [outY, inf],
        colors='w'
    )
    ax[1,1].contourf(
        theta_mesh, phi_mesh,
        inX*sin(phi_mesh) + inZ*cos(phi_mesh),
        [outZ, inf],
        colors='w'
    )

def submitOutX(text):
    global outX
    outX = float(text)
    draw_X()
    draw_all()

def submitOutY(text):
    global outY
    outY = float(text)
    draw_Y()
    draw_all()

def submitOutZ(text):
    global outZ
    outZ = float(text)
    draw_Z()
    draw_all()

def submitInX(text):
    global inX
    inX = float(text)
    draw_X()
    draw_Y()
    draw_Z()
    draw_all()

def submitInY(text):
    global inY
    inY = float(text)
    draw_X()
    draw_Y()
    #draw_Z()
    draw_all()

def submitInZ(text):
    global inZ
    inZ = float(text)
    draw_X()
    draw_Y()
    draw_Z()
    draw_all()


def get_rect_prism(a, b, c):
    return np.array([[-a, -b, -c], [-a, -b, c], [-a, b, -c],  [a, -b, -c], [a, b, -c], [a, -b, c], [-a, b, c], [a, b, c]])
def get_faces(v):
    return [ [v[0],v[2],v[6],v[1]], [v[0],v[3],v[4],v[2]], [v[0],v[1],v[5],v[3]],
             [v[7],v[5],v[1],v[6]], [v[7],v[6],v[2],v[4]], [v[7],v[4],v[3],v[5]] ]

def draw_rect(theta, phi):
    global ax3d
    ax3d.clear()

    outV = get_rect_prism(outX, outY, outZ)
    out_faces = get_faces(outV)
    ax3d.add_collection3d(Poly3DCollection(out_faces, facecolors='black', linewidths=1, edgecolors='k', alpha=0.5))

    inV = get_rect_prism(inX, inY, inZ)
    r = R.from_euler('yz', [-phi, theta], degrees=False)
    inV = np.array([ r.apply(pnt) for pnt in inV ])
    in_faces = get_faces(inV)
    ax3d.add_collection3d(Poly3DCollection(in_faces, facecolors='red', linewidths=1, edgecolors='k'))

    ax3d.scatter3D([-10, 10], [-10, 10], [-10, 10])
    ax3d.set_xlabel('x')
    ax3d.set_ylabel('y')
    ax3d.set_zlabel('z')
    ax3d.set_xticklabels([])
    ax3d.set_yticklabels([])
    ax3d.set_zticklabels([])
    ax3d.set_ylim(ax3d.get_ylim()[::-1])

    plt.draw()

def onclick(event):
    theta = event.xdata
    phi = event.ydata
    if theta is not None and phi is not None:
        draw_rect(theta, phi)


fig, ax = plt.subplots(2, 4, figsize=(16, 8))
for row in ax:
    for col in row:
        col.axis('off')
        col.axis('off')

plt.subplots_adjust(bottom=0.2)
ax3d = fig.add_subplot(122, projection='3d')

inf = 1000
outX = 5
outY = 5
outZ = 5
inX = 7
inY = 0.5
inZ = 0.5

delta = 0.1
theta_mesh, phi_mesh = meshgrid(
    arange(0, pi/2, delta),
    arange(0, pi/2, delta)
)

outXax = plt.axes([0.1, 0.05, 0.05, 0.075])
outXbox = TextBox(outXax, 'Outer X', initial=str(outX))
outXbox.on_submit(submitOutX)

outYax = plt.axes([0.25, 0.05, 0.05, 0.075])
outYbox = TextBox(outYax, 'Outer Y', initial=str(outY))
outYbox.on_submit(submitOutY)

outZax = plt.axes([0.4, 0.05, 0.05, 0.075])
outZbox = TextBox(outZax, 'Outer Z', initial=str(outZ))
outZbox.on_submit(submitOutZ)

inXax = plt.axes([0.55, 0.05, 0.05, 0.075])
inXbox = TextBox(inXax, 'Inner X', initial=str(inX))
inXbox.on_submit(submitInX)

inYax = plt.axes([0.7, 0.05, 0.05, 0.075])
inYbox = TextBox(inYax, 'Inner Y', initial=str(inY))
inYbox.on_submit(submitInY)

inZax = plt.axes([0.85, 0.05, 0.05, 0.075])
inZbox = TextBox(inZax, 'Inner Z', initial=str(inZ))
inZbox.on_submit(submitInZ)

draw_X()
draw_Y()
draw_Z()
draw_all()
draw_rect(0, 0)

fig.canvas.set_window_title('Box Fits Inside Box')
fig.suptitle('Click the Subplots!')
fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()
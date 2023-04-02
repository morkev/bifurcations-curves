import bpy
import math

# mesh arrays
vertices = []
faces = []

# mesh variables
numX = 100
numY = 100

# fill vertices array
for i in range(0, numX):
    for j in range(0, numY):
        # normalize range
        x = (i / numX * 4) - 2
        y = (j / numY * 4) - 2

        zx = 0
        zy = 0

        for it in range(0, 255):
            xt = zx * zy
            zx = zx * zx - zy * zy + x
            zy = 2 * xt + y
            if zx * zx + zy * zy > 4:
                break
        z = math.log1p(it)

        vertices = (x, y, z)
        verts.append(vert)

# fill faces array
count = 0
for i in range(0, numY * (numX - 1)):
    if count < numY - 1:
        A = i
        B = i + 1
        C = (i + numY) + 1
        D = (i + numY)
        face = (A, B, C, D)
        faces.append(face)
        count = count + 1
    else:
        count = 0

# create mesh and object
mesh = bpy.data.meshes.new("mandelbrot")
object = bpy.data.objects.new("mandelbrot", mesh)

# set mesh location
object.location = bpy.context.scene.cursor.location
bpy.context.scene.objects.link(object)

# create mesh from python data
mesh.from_pydata(verts, [], faces)
mesh.update(calc_edges=True)
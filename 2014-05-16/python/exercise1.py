from larcc import *

def makeColor(r,g,b):
	red = (float(r)/255)
	green = (float(g)/255)
	blue = (float(b)/255)
	print red,green,blue
	return Color4f([red,green,blue,1])

def makeHole(master,color):
	hpc = SKEL_1(STRUCT(MKPOLS(master)))
	hpc = cellNumbering (master,hpc)(range(len(master[1])),color,2)
	return hpc

gold = makeColor(255,215,0)
glass = [0.1,0.2,0.3,1,  0,0,0,0.5,  2,2,2,1, 0,0,0,1, 100]

DRAW = COMP([VIEW,STRUCT,MKPOLS])
master = assemblyDiagramInit([9,9,2])([[.5,3.8,.2,5.8,0.2,3.8,.2,4.8,.5],[.2,4,.5,5.8,.2,6.8,.2,7.8,.5],[0.3,3.2]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),gold,2)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),gold,2)

# making all the door of the house

zaxe = [2.2,1]

toMerge = 11
diagram = assemblyDiagramInit([1,3,2])([[.5],[1.9,3,1.9],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)

toMerge = 26
diagram = assemblyDiagramInit([3,1,2])([[1.4,1,1.4],[.2],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)

toMerge = 61
diagram = assemblyDiagramInit([3,1,2])([[1.3,1,3.5],[.2],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)

toMerge = 64
diagram = assemblyDiagramInit([3,1,2])([[1.9,2,1.9],[.2],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)

toMerge = 79
diagram = assemblyDiagramInit([1,3,2])([[.2],[2.4,2,2.4],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)

toMerge = 98
diagram = assemblyDiagramInit([3,1,2])([[1.4,1,1.4],[.2],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)

toMerge = 113
diagram = assemblyDiagramInit([1,3,2])([[.2],[4.3,1,1.5],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)

toMerge = 128
diagram = assemblyDiagramInit([3,1,2])([[1.9,1,1.9],[.2],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)

# making all the windows of the house

zaxe = [1,1.4,.8]

toMerge = 22
diagram = assemblyDiagramInit([3,1,3])([[1.5,0.8,1.5],[.2],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)

toMerge = 56
diagram = assemblyDiagramInit([3,1,2])([[2.1,1.6,2.1],[.2],[2.2,1]])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)

toMerge = 65
diagram = assemblyDiagramInit([3,1,3])([[2,1.8,2],[.5],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)

toMerge = 98
diagram = assemblyDiagramInit([3,1,3])([[1.8,1.6,1.8],[.5],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)

toMerge = 139
diagram = assemblyDiagramInit([1,3,3])([[.5],[1.9,1.2,2.7],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)

toMerge = 142
diagram = assemblyDiagramInit([1,3,3])([[.5],[1.6,1.5,3.7],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)

# making the balcony

zaxe = [1.6,2]

toMerge = 36
diagram = assemblyDiagramInit([1,1,2])([[.2],[.2],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)

toMerge = 34
diagram = assemblyDiagramInit([1,1,2])([[.2],[4],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)

toMerge = 50
diagram = assemblyDiagramInit([1,1,2])([[5.8],[.2],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)

toMerge = 63
diagram = assemblyDiagramInit([1,1,2])([[.2],[.2],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)

toMerge = 64
diagram = assemblyDiagramInit([1,1,2])([[.2],[4],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)

toRemoveForBalcony = [0,1,2,3,17,18,19,20,51,77,78,79,80,93,94,95,96,110,111,112,113,127,128,129,130]
balcony = [243,245,247,249,251]
rooms = [23,26,30,42,46,54,57,60,88,91,117,120]
doors = [145,151,157,163,169,175,181,187]
windows = [195,202,210,219,228,237]
toRemove = toRemoveForBalcony+balcony+rooms+doors+windows
apartment = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]

# DRAW(apartment)
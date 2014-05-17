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

DRAW = COMP([VIEW,STRUCT,MKPOLS])
master = assemblyDiagramInit([9,7,2])([[.5,3.8,.2,5.8,0.2,3.8,.2,4.8,.5],[.5,5.8,.2,6.8,.2,7.8,.5],[0.3,3.2]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),gold,2)

toRemove = [17,45,101,21,35,49,77,105,25,39,53,81]
master = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]


hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),gold,2)

# making all the door of the house

zaxe = [2.2,1]

toMerge = 7
diagram = assemblyDiagramInit([1,3,2])([[.5],[1.9,3,1.9],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)

toMerge = 17
diagram = assemblyDiagramInit([3,1,2])([[1.4,1,1.4],[.2],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)

toMerge = 39
diagram = assemblyDiagramInit([3,1,2])([[1.3,1,3.5],[.2],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)

toMerge = 41
diagram = assemblyDiagramInit([3,1,2])([[1.9,2,1.9],[.2],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)


toMerge = 51
diagram = assemblyDiagramInit([1,3,2])([[.2],[2.4,2,2.4],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)

toMerge = 65
diagram = assemblyDiagramInit([3,1,2])([[1.4,1,1.4],[.2],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)

toMerge = 75
diagram = assemblyDiagramInit([1,3,2])([[.2],[4.3,1,1.5],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)

toMerge = 85
diagram = assemblyDiagramInit([3,1,2])([[1.9,1,1.9],[.2],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)

toRemove = [108,114,120,126,132,138,144,150]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]


# making all the windows of the house

zaxe = [1,1.4,.8]

toMerge = 14
diagram = assemblyDiagramInit([3,1,3])([[1.5,0.8,1.5],[.2],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)

toMerge = 35
diagram = assemblyDiagramInit([3,1,3])([[2.1,1.6,2.1],[.2],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)

toMerge = 41
diagram = assemblyDiagramInit([3,1,3])([[2,1.8,2],[.5],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)

toMerge = 64
diagram = assemblyDiagramInit([3,1,3])([[1.8,1.6,1.8],[.5],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)

toMerge = 91
diagram = assemblyDiagramInit([1,3,3])([[.5],[1.9,1.2,2.7],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)

toMerge = 94
diagram = assemblyDiagramInit([1,3,3])([[.5],[1.6,1.5,3.7],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)

toRemove = [144,153,162,171,180,189,198]
apartment = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
# DRAW(master)
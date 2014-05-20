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

toRemove = [21,25,29,33,57,61,65,69,93,97,101,105,129,133,137,141]
master = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]


hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),gold,2)

# making all the door of the house

zaxe = [2.2,1]

toMerge = 11
diagram = assemblyDiagramInit([1,3,2])([[.5],[1.9,3,1.9],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)
# VIEW(hpc)

toMerge = 24
diagram = assemblyDiagramInit([3,1,2])([[1.4,1,1.4],[.2],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)
# VIEW(hpc)

toMerge = 55
diagram = assemblyDiagramInit([3,1,2])([[1.3,1,3.5],[.2],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)
# VIEW(hpc)

toMerge = 57
diagram = assemblyDiagramInit([3,1,2])([[1.9,2,1.9],[.2],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)
# VIEW(hpc)

toMerge = 71
diagram = assemblyDiagramInit([1,3,2])([[.2],[2.4,2,2.4],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)
# VIEW(hpc)

toMerge = 87
diagram = assemblyDiagramInit([3,1,2])([[1.4,1,1.4],[.2],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)
# VIEW(hpc)

toMerge = 101
diagram = assemblyDiagramInit([1,3,2])([[.2],[4.3,1,1.5],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)

toMerge = 114
diagram = assemblyDiagramInit([3,1,2])([[1.9,1,1.9],[.2],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)
# VIEW(hpc)

toRemove = [140,146,152,158,164,170,176,182]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
# DRAW(master)

# # making all the windows of the house

zaxe = [1,1.4,.8]

toMerge = 21
diagram = assemblyDiagramInit([3,1,3])([[1.5,0.8,1.5],[.2],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)
# VIEW(hpc)

toMerge = 51
diagram = assemblyDiagramInit([3,1,2])([[2.1,1.6,2.1],[.2],[2.2,1]])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)
# VIEW(hpc)

toMerge = 57
diagram = assemblyDiagramInit([3,1,3])([[2,1.8,2],[.5],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)
# VIEW(hpc)

toMerge = 86
diagram = assemblyDiagramInit([3,1,3])([[1.8,1.6,1.8],[.5],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)
# VIEW(hpc)

toMerge = 123
diagram = assemblyDiagramInit([1,3,3])([[.5],[1.9,1.2,2.7],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)
# VIEW(hpc)

toMerge = 126
diagram = assemblyDiagramInit([1,3,3])([[.5],[1.6,1.5,3.7],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)
# VIEW(hpc)

toRemove = [176,183,191,200,209,218]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]

# making the balcony
toRemove = [0,1,2,3,17,18,19,74,75,76,86,87,88,89,103,104,105,116,117,118,119]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]

zaxe = [1.6,2]

toMerge = 23
diagram = assemblyDiagramInit([1,1,2])([[.2],[.2],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)
# VIEW(hpc)

toMerge = 24
diagram = assemblyDiagramInit([1,1,2])([[.2],[4],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)
# VIEW(hpc)

toMerge = 39
diagram = assemblyDiagramInit([1,1,2])([[5.8],[.2],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)
# VIEW(hpc)

toMerge = 48
diagram = assemblyDiagramInit([1,1,2])([[.2],[.2],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)
# VIEW(hpc)

toMerge = 49
diagram = assemblyDiagramInit([1,1,2])([[.2],[4],zaxe])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)
# VIEW(hpc)

toRemove = [192,194,196,198,200]
apartment = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]

# DRAW(apartment)
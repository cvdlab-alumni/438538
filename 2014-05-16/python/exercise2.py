from exercise1 import *
from larcc import *

brown = makeColor(101,67,33)
forest = makeColor(34,139,34)

def makeStairs(l1,l2,l3):
	stairs = []
	j = l2/5
	for i in range(1,l2):
		steps = T([2,3])([i,i*l3])(CUBOID([l1,j,l3]))
		stairs = stairs+[steps]
	return stairs

def makeBars(l1,h):
	bars_x = QUOTE([-.15,.2,-.15]*(l1*2))
	bars_y = QUOTE([0.2])
	bars_z = QUOTE([h])
	bars1 = INSR(PROD)([bars_x,bars_y,bars_z])
	bars_x = QUOTE([l1])
	bars_y = QUOTE([.2])
	bars_z = QUOTE([-h,.2])
	bars2 = INSR(PROD)([bars_x,bars_y,bars_z])
	bars = STRUCT([bars1,bars2])
	return bars

def makeCurve(controlpoints):
	domain = larDomain([32])
	mapping = larBezierCurve(controlpoints)
	obj = larMap(mapping)(domain)
	return STRUCT(MKPOLS(obj))

def makeTree(coordinate):
	bx,by = coordinate
	def makeTree0(dimensions):
		r,h = dimensions
		trunk = CYLINDER ([r,h])(50)
		chioma = SPHERE(r*3.5)([32,32])
		trunk = COLOR(brown)(STRUCT([trunk]))
		chioma = COLOR(forest)(STRUCT([chioma]))
		return T([1,2])([bx,by])(STRUCT([trunk,T(3)(h+r)(chioma)]))
	return makeTree0

green = makeColor(1,121,111)
grey = makeColor(147,147,147)
glass = [0.1,0.2,0.3,1,  0,0,0,0.5,  2,2,2,1, 0,0,0,1, 100]

apartmentRotate = larApply(s(-1,1,1))(apartment)
apartmentRotate = larApply(t(19.8,0,0))(apartmentRotate)

master = assemblyDiagramInit([3,1,11])([[19.8,8,19.8],[21.8],[.5,3.5,.5,3.5,.5,3.5,.5,3.5,.5,3.5,.5]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),gold,2)

toRemove = [12,14,16,18,20]
master = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),gold,2)

toMerge = 12
diagram = assemblyDiagramInit([3,3,1])([[2,4,2],[2,10,7.8],[0.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)


toMerge = 12
diagram = assemblyDiagramInit([3,3,1])([[2,4,2],[2,10,7.8],[0.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)

toMerge = 12
diagram = assemblyDiagramInit([3,3,1])([[2,4,2],[2,10,7.8],[0.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)


toMerge = 12
diagram = assemblyDiagramInit([3,3,1])([[2,4,2],[2,10,7.8],[0.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)

toRemove = [12,28,37,46,55]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),gold,2)


toMerge = 13
master = diagram2cell(apartment,master,toMerge)
hpc = makeHole(master,gold)

toMerge = 14
master = diagram2cell(apartment,master,toMerge)
hpc = makeHole(master,gold)

toMerge = 15
master = diagram2cell(apartment,master,toMerge)
hpc = makeHole(master,gold)

toMerge = 16
master = diagram2cell(apartment,master,toMerge)
hpc = makeHole(master,gold)

toMerge = 17
master = diagram2cell(apartment,master,toMerge)
hpc = makeHole(master,gold)

toMerge = 1
master = diagram2cell(apartmentRotate,master,toMerge)
hpc = makeHole(master,gold)

toMerge = 2
master = diagram2cell(apartmentRotate,master,toMerge)
hpc = makeHole(master,gold)

toMerge = 3
master = diagram2cell(apartmentRotate,master,toMerge)
hpc = makeHole(master,gold)

toMerge = 4
master = diagram2cell(apartmentRotate,master,toMerge)
hpc = makeHole(master,gold)

toMerge = 5
master = diagram2cell(apartmentRotate,master,toMerge)
hpc = makeHole(master,gold)

condominium = (STRUCT(MKPOLS(master)))

stairs = STRUCT(makeStairs(4,10,.4))
stairs1 = T([1,2,3])([21.8,2,.5])(stairs)
stairs2 = T([1,2,3])([21.8,2,4.5])(stairs)
stairs3 = T([1,2,3])([21.8,2,8.5])(stairs)
stairs4 = T([1,2,3])([21.8,2,12.5])(stairs)
stairs = STRUCT([stairs1,stairs2,stairs3,stairs4])

bars = makeBars(8,1)
bars1 = T([1,2,3])([19.8,21.6,.5])(bars)
bars2 = T([1,2,3])([19.8,0,4.5])(bars)
bars3 = T([1,2,3])([19.8,21.6,4.5])(bars)
bars4 = T([1,2,3])([19.8,0,8.5])(bars)
bars5 = T([1,2,3])([19.8,21.6,8.5])(bars)
bars6 = T([1,2,3])([19.8,0,12.5])(bars)
bars7 = T([1,2,3])([19.8,21.6,12.5])(bars)
bars8 = T([1,2,3])([19.8,0,16.5])(bars)
bars9 = T([1,2,3])([19.8,21.6,16.5])(bars)
bars = STRUCT([bars1,bars2,bars3,bars4,bars5,bars6,bars7,bars8,bars9])

condominium = T([1,2])([20,25])(STRUCT([condominium,stairs,bars]))

lawnColor = makeColor(152,255,152)

lawn_x = QUOTE([87.6])
lawn_y = QUOTE([50])
lawn_z = QUOTE([.3])
lawn = COLOR(lawnColor)(INSR(PROD)([lawn_x,lawn_y,lawn_z]))

c1 = makeCurve([[1.96, 4.432], [-0.119, 4.181], [0.898, 1.189], [1.987, 0.875]])
c2 = makeCurve([[1.987, 0.875], [2.526, 0.922], [2.57, 1.095], [2.83, 1.065]])
c3 = makeCurve([[2.83, 1.065], [3.007, 1.168], [3.475, 0.843], [3.631, 0.883]])
c4 = makeCurve([[3.631, 0.883], [4.114, 0.858], [4.604, 1.606], [4.773, 2.137]])
c5 = makeCurve([[4.773, 2.137], [4.054, 2.42], [3.801, 3.453], [4.628, 3.97]])
c6 = makeCurve([[4.628, 3.97], [4.382, 4.385], [3.961, 4.425], [3.824, 4.441]])
c7 = makeCurve([[3.824, 4.441], [3.386, 4.501], [2.874, 4.163], [2.797, 4.224]])
c8 = makeCurve([[2.797, 4.224], [2.345, 4.284], [2.356, 4.454], [1.96, 4.427]])
c9 = makeCurve([[2.836, 4.555], [2.768, 5.206], [3.344, 5.522], [3.871, 5.606]])
c10 = makeCurve([[3.871, 5.606], [3.88, 5.321], [3.757, 4.568], [2.833, 4.544]])

apple1 = T([1,2,3])([25,8,.51])(S([1,2])([2.5,2.5])(STRUCT([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10])))
apple2 = T(1)(25)(apple1)
apple = COLOR(green)(STRUCT([apple1,apple2]))

c1 = makeCurve([[10,10],[2.5,11],[2.49,23],[2.5,25]])
c2 = makeCurve([[2.5,25],[2.49,27],[2.5,39],[10,40]])
c3 = makeCurve([[10,40],[17.5,39],[17.51,27],[17.5,25]])
c4 = makeCurve([[17.5,25],[17.51,23],[17.5,11],[10,10]])
lake = STRUCT([c1,c2,c3,c4])
lake = T(3)(.6)(MATERIAL(glass)(SOLIDIFY(lake)))

sidewalk_x = QUOTE([-20,-19.8,8])
sidewalk_y = QUOTE([25])
sidewalk_z = QUOTE([-.5,.3])
sidewalk = COLOR(grey)(INSR(PROD)([sidewalk_x,sidewalk_y,sidewalk_z]))


tree1 = makeTree([80,5])([1.5,10])
tree2 = makeTree([80,18])([1.5,11.6])
tree3 = makeTree([80,31])([1.5,13.2])
tree4 = makeTree([80,44])([1.5,15])
tree = STRUCT([tree1,tree2,tree3,tree4])

VIEW(STRUCT([condominium,apple,lawn,sidewalk,lake,tree]))
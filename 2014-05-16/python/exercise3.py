from larcc import *
 
DRAW = COMP([VIEW,STRUCT,MKPOLS])
 
def mergingNumberingElimination(diagramHole,diagram,toMerge,toRemove):
	diagramHole = diagramHole[0],[cell for k,cell in enumerate(diagramHole[1]) if not (k in toRemove)]
	toMerge = list(sort(toMerge))
	iterate = range(len(toMerge))
	for i in iterate:
		elementToMerge = toMerge[i]-i
		diagram = diagram2cell(diagramHole,diagram,elementToMerge)
	return diagram
 
# example


# main structure
shape = [7,7,1]
sizePatterns = [[.5,3]*3+[.5],[.5,3]*3+[.5],[5]]
master = assemblyDiagramInit(shape)(sizePatterns)
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
toRemove = [8,10,12,22,24,26,36,38,40]
master = master[0],[cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
# VIEW(hpc)
# DRAW(master)

#create a window
shape = [3,1,3]
sizePatterns = [[1.1,.8,1.1],[.5],[2,2,1]]
window = assemblyDiagramInit(shape)(sizePatterns)
V,CV = window
hpc = SKEL_1(STRUCT(MKPOLS(window)))
hpc = cellNumbering (window,hpc)(range(len(CV)),CYAN,2)
# VIEW(hpc)
# DRAW(window)
 
# create many windows in main structure
master = mergingNumberingElimination(window,master,[7,18,29,10,21,32],[4])
 
# main structure after create windows
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
# VIEW(hpc)
# DRAW(master)
from pyplasm import *
from larcc import *
from exercise3 import *

brown = makeColor(101,67,33)
forest = makeColor(34,139,34)
water = makeColor(30,144,255)
silver = makeColor(192,192,192)
yellow = makeColor(255,255,0)

def makeTree(coordinate):
	bx,by = coordinate
	def makeTree0(dimensions):
		r,h = dimensions
		tronco = larCylinder(dimensions)([32,1])
		chioma = larSphere(r*4)()
		tronco = COLOR(brown)(STRUCT(MKPOLS(tronco)))
		chioma = COLOR(forest)(STRUCT(MKPOLS(chioma)))
		return T([1,2])([bx,by])(STRUCT([tronco,T(3)(h+r)(chioma)]))
	return makeTree0

def makeStreetLamp(coordinate):
	bx,by = coordinate
	palo = larCylinder([0.3,10])([32,1])
	luce = larSphere(0.7)()
	palo = COLOR(silver)(STRUCT(MKPOLS(palo)))
	luce = COLOR(yellow)(STRUCT(MKPOLS(luce)))
	return T([1,2])([bx,by])(STRUCT([palo,T(3)(10)(luce)]))


#creazione delle linee del campo di calcio
line_field1_x =  QUOTE([-29.6,0.4,-59.8,0.4,-59.8,0.4])
line_field1_y = QUOTE([-35,90])
line_field_z = QUOTE([0.3])
line_field1 = (INSR)(PROD)([line_field1_x,line_field1_y,line_field_z])
line_field2_x = QUOTE([-30,120])
line_field2_y = QUOTE([-34.6,0.4,-90,0.4])
line_field2 = (INSR)(PROD)([line_field2_x,line_field2_y,line_field_z])
line_field3_x = QUOTE([-30,20,-80,20])
line_field3_y = QUOTE([-59.6,0.4,-40,0.4])
line_field3 = (INSR)(PROD)([line_field3_x,line_field3_y,line_field_z])
line_field4_x = QUOTE([-49.6,0.4,-80,0.4])
line_field4_y = QUOTE([-60,40])
line_field4 = (INSR)(PROD)([line_field4_x,line_field4_y,line_field_z])
line_field5 = T([1,2,3])([90,80,0.4])(CIRCUMFERENCE(10)(32))
line_field6_x = QUOTE([-30,10,-100,10])
line_field6_y = QUOTE([-69.6,0.4,-20,0.4])
line_field6 = (INSR)(PROD)([line_field6_x,line_field6_y,line_field_z])
line_field7_x = QUOTE([-39.6,0.4,-100,0.4])
line_field7_y = QUOTE([-70,20])
line_field7 = (INSR)(PROD)([line_field7_x,line_field7_y,line_field_z])
door1_x = QUOTE([-27.6,0.4,-1.6,0.4,-120,0.4,-1.6,0.4])
door1_y = QUOTE([-74.6,0.4,-10,0.4])
door1 = (INSR)(PROD)([door1_x,door1_y,QUOTE([2])])
door2_y = QUOTE([-74.6,10.8])
door2 = T(3)(2)((INSR)(PROD)([door1_x,door2_y,QUOTE([0.4])]))
door3_x = QUOTE([-27.6,2.4,-120,2.4])
door3 = T(3)(2)((INSR)(PROD)([door3_x,door1_y,QUOTE([0.4])]))
door = STRUCT([door1,door2,door3])
stadium = COLOR(WHITE)(STRUCT([line_field1,line_field2,line_field3,line_field4,line_field5,line_field6,line_field7,door]))

# arredamento del parco
lake = checkModel(larDisk(20)([36,4]))
lake = STRUCT(MKPOLS(lake))
lake = COLOR(water)(PROD([lake,QUOTE([0.5])]))
lake = T([1,2])([260,260])(lake)
tree1 = makeTree([220,220])([2,24])
tree2 = makeTree([220,250])([2,24])
tree3 = makeTree([220,280])([2,24])
tree4 = makeTree([250,220])([2,24])
tree5 = makeTree([280,220])([2,24])
tree = STRUCT([tree1,tree2,tree3,tree4,tree5])
park = STRUCT([lake,tree])

# arredamento del parcheggio
tree1 = makeTree([220,45])([2,24])
tree2 = makeTree([250,45])([2,24])
tree = STRUCT([tree1,tree2])
line_parking1_x = QUOTE([-195,80])
line_parking1_y = QUOTE([-24.5,0.5,-40,0.5])
line_parking1 = (INSR)(PROD)([line_parking1_x,line_parking1_y,line_field_z])
line_parking2_x = QUOTE([-3.5,0.5]*19)
line_parking2_y = QUOTE([-15,10,-40,10])
line_parking2 = T(1)(195)((INSR)(PROD)([line_parking2_x,line_parking2_y,line_field_z]))
line_parking = COLOR(WHITE)(STRUCT([line_parking1,line_parking2]))
parking = STRUCT([tree,line_parking])

# illuminazione
lamp1 = makeStreetLamp([31,241])
lamp2 = makeStreetLamp([65,241])
lamp3 = makeStreetLamp([31,289])
lamp4 = makeStreetLamp([65,289])

lamp5 = makeStreetLamp([91,241])
lamp6 = makeStreetLamp([128,241])
lamp7 = makeStreetLamp([91,274])
lamp8 = makeStreetLamp([128,274])

lamp9 = makeStreetLamp([151,241])
lamp10 = makeStreetLamp([183,241])
lamp11 = makeStreetLamp([151,274])
lamp12 = makeStreetLamp([183,274])

lamp13 = makeStreetLamp([31,181])
lamp14 = makeStreetLamp([65,181])
lamp15 = makeStreetLamp([31,214])
lamp16 = makeStreetLamp([65,214])

lamp17 = makeStreetLamp([151,181])
lamp18 = makeStreetLamp([200,181])
lamp19 = makeStreetLamp([151,214])
lamp20 = makeStreetLamp([200,214])

lamp21 = makeStreetLamp([191,141])
lamp22 = makeStreetLamp([225,141])
lamp23 = makeStreetLamp([191,174])
lamp24 = makeStreetLamp([225,174])

lamp25 = makeStreetLamp([241,141])
lamp26 = makeStreetLamp([290,141])
lamp27 = makeStreetLamp([241,199])
lamp28 = makeStreetLamp([290,199])

lamp29 = makeStreetLamp([191,91])
lamp30 = makeStreetLamp([225,91])
lamp31 = makeStreetLamp([191,124])
lamp32 = makeStreetLamp([225,124])

lamp33 = makeStreetLamp([241,91])
lamp34 = makeStreetLamp([275,91])
lamp35 = makeStreetLamp([241,124])
lamp36 = makeStreetLamp([275,124])

lamp37 = makeStreetLamp([82,172])
lamp38 = makeStreetLamp([82,182])
lamp39 = makeStreetLamp([82,192])
lamp40 = makeStreetLamp([82,202])
lamp41 = makeStreetLamp([82,212])
lamp42 = makeStreetLamp([128,172])
lamp43 = makeStreetLamp([128,182])
lamp44 = makeStreetLamp([128,192])
lamp45 = makeStreetLamp([128,202])
lamp46 = makeStreetLamp([128,212])

lamps = STRUCT([lamp1,lamp2,lamp3,lamp4,lamp5,lamp6,lamp7,lamp8,lamp9,lamp10,lamp11,lamp12,lamp13,lamp14,lamp15,lamp16,lamp17,lamp18,lamp19,lamp20,
	lamp21,lamp22,lamp23,lamp24,lamp25,lamp26,lamp27,lamp28,lamp29,lamp30,lamp31,lamp32,lamp33,lamp34,lamp35,lamp36,lamp37,lamp38,lamp39,lamp40,
	lamp41,lamp42,lamp43,lamp44,lamp45,lamp46])

tree1 = makeTree([10,10])([2,24])
tree2 = makeTree([10,40])([2,24])
tree3 = makeTree([10,70])([2,24])
tree4 = makeTree([10,100])([2,24])
tree5 = makeTree([10,130])([2,24])
tree6 = makeTree([10,160])([2,24])
tree7 = makeTree([10,190])([2,24])
tree8 = makeTree([10,220])([2,24])
tree9 = makeTree([10,250])([2,24])
tree10 = makeTree([10,280])([2,24])
trees = STRUCT([tree1,tree2,tree3,tree4,tree5,tree6,tree7,tree8,tree9,tree10])

urbanFittings = STRUCT([neighbouringBuildings,stadium,park,parking,lamps,trees])
VIEW(urbanFittings)


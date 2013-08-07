import random
a = [((1,2),(3,4)) , ((6,7),(8,9)) , ((11,12),(13,14)) , ((1,2),(6,7))]
print a
spot = random.choice(a)
a.pop(a.index(spot))
print spot[0]
print spot[1]
for coord in a:
	xy1, xy2 = coord
        if xy1 == spot[0] or xy1 == spot[1] or xy2 == spot[0] or xy2 == spot[1]:
            a.pop(a.index(coord))
	#for value in coord:
	#	if value == spot[0] or value == spot[1]:
	#		a.pop(a.index(coord))
print a
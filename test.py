import random
import pprint
pp = pprint.PrettyPrinter(depth=6)

a = [((1,2),(3,4)) , ((6,7),(8,9)) , ((11,12),(13,14)) , ((1,2),(6,7))]
pp.pprint(a)

spot = random.choice(a)
print 'Grabbed random spot: {0}'.format(spot)

print 'Removing {0} from list'
a.pop(a.index(spot))
pp.pprint(a)


print 'Looping over the spots to find rest of interesting spots'
for coord in a:
    xy1, xy2 = coord
    print 'Looking for spots: {0} and {1}'.format(xy1, xy2)
    if xy1 == spot[0] or xy1 == spot[1] or xy2 == spot[0] or xy2 == spot[1]:
        val_popped = a.pop(a.index(coord))
        print 'Matched spot: {0}'.format(val_popped)
    #for value in coord:
    #   if value == spot[0] or value == spot[1]:
    #       a.pop(a.index(coord))
pp.pprint(a)
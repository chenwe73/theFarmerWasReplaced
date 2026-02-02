import utils

gain = 2**9
polyculture = 160

def single():
    n = 100000000
    cycles = n // gain // polyculture + 1
    x, y = 3, 3
    utils.move_to(x, y)
    for i in range(cycles):
        companion, (xc, yc) = get_companion()
        utils.move_to(xc, yc)
        if get_ground_type() == Grounds.Grassland:
            till()
        plant(companion)
        utils.move_to(x, y)
        harvest()

single()

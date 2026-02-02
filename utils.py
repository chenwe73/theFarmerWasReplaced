DIRECTIONS = [North, East, South, West]
VECTORS = [(0,1), (1,0), (0,-1), (-1,0)]
num_moves = 0

def idle(ent=Items.Hay):
    while True:
        start = num_items(ent)
        for i in range(1):
            print("!")
        end = num_items(ent)
        quick_print(end - start)

def move_straight(steps, dir):
    global num_moves
    result = True
    for i in range(steps):
        r = move(dir)
        if not r:
            result = False
        else:
            num_moves += 1
    return result

def move_to(x=0, y=0):
    dy = y - get_pos_y()
    dir = {True: North, False: South}[dy > 0]
    ry = move_straight(abs(dy), dir)
    dx = x - get_pos_x()
    dir = {True: East, False: West}[dx > 0]
    rx = move_straight(abs(dx), dir)
    return rx and ry

def is_stuck():
    result = True
    for d in DIRECTIONS:
        if can_move(d):
            result = False
    return result

def get_pos():
    return (get_pos_x(), get_pos_y())

def dist(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

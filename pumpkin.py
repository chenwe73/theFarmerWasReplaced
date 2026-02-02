import utils

cols, rows = 4, 8
w = get_world_size() // cols
h = get_world_size() // rows

def drone():
    x, y = get_pos_x(), get_pos_y()
    while True:
        is_full = True
        for i in range(w):
            for j in range(h):
                utils.move_to(x+i, y+j)
                if get_ground_type() == Grounds.Grassland:
                    till()
                if get_entity_type() in [None, Entities.Dead_Pumpkin]:
                    plant(Entities.Pumpkin)
                    is_full = False
        # if is_full:
        #     harvest()

def main():
    for i in range(cols):
        for j in range(rows):
            utils.move_to(i * w, j * h)
            if (i, j) == (cols-1, rows-1):
                break
            spawn_drone(drone)
    drone()

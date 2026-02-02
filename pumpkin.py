import utils

def main(size=6):
    x, y = get_pos_x(), get_pos_y()
    while True:
        is_full = True
        for i in range(size):
            for j in range(size):
                utils.move_to(x+i, y+j)
                if get_ground_type() == Grounds.Grassland:
                    till()
                if get_entity_type() in [None, Entities.Dead_Pumpkin]:
                    plant(Entities.Pumpkin)
                    is_full = False
        if is_full:
            harvest()

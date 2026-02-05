import utils

cols, rows = 4, 8
w = get_world_size() // cols
h = get_world_size() // rows
min_water = 0.75
item = Items.Pumpkin

def drone():
    x, y = get_pos_x(), get_pos_y()
    last_id = 0
    while True:
        is_full = True
        for i in range(w):
            for j in range(h):
                utils.move_to(x+i, y+j)
                if get_ground_type() == Grounds.Grassland:
                    till()
                if get_entity_type() == None:
                    plant(Entities.Pumpkin)
                    is_full = False
                if get_entity_type() == Entities.Dead_Pumpkin:
                    plant(Entities.Pumpkin)
                    is_full = False
                    # use_item(Items.Fertilizer)
                    # use_item(Items.Weird_Substance)
                while get_water() < min_water:
                    use_item(Items.Water)
                id = measure()
                if id != last_id:
                    is_full = False
                last_id = id
        if is_full:
            harvest()

def patrol():
    size = 6
    last_id = 0
    count = 0
    while True:
        for i in range(0, get_world_size(), size):
            utils.move_to(0, i)
            for j in range(get_world_size()):
                id = measure()
                if id == last_id:
                    count += 1
                else:
                    count = 0
                last_id = id
                if count >= size:
                    harvest()
                    count = 0
                move(East)
            move(East)

def main():
    for i in range(cols):
        for j in range(rows):
            utils.move_to(i * w, j * h)
            if (i, j) == (cols-1, rows-1):
                break
            spawn_drone(drone)
    drone()


if __name__ == "__main__":
    main()

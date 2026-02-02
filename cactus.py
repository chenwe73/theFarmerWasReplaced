import utils

min_water = 0.75
ent = Entities.Cactus

def simple():
    x, y = get_pos_x(), get_pos_y()
    cols = 8
    while True:
        for i in range(0, cols, 2):
            utils.move_to(x+i, y)
            cactus_sizes = []
            for j in range(2):
                utils.move_to(x+i, y+j)
                if get_ground_type() == Grounds.Grassland:
                    till()
                if get_entity_type() == None:
                    plant(ent)
                    m = measure()
                    cactus_sizes.append(m)
                while get_water() < min_water:
                    use_item(Items.Water)
            if cactus_sizes[0] > cactus_sizes[1]:
                swap(South)
        for i in range(0, cols, 2):
            utils.move_to(x+i, y)
            while not can_harvest():
                print("!")
            harvest()

def same():
    rows, cols = 4, 8
    cactus_size = 9
    x, y = get_pos_x(), get_pos_y()
    for i in range(cols):
        for j in range(rows):
            utils.move_to(x+i, y+j)
            if get_ground_type() == Grounds.Grassland:
                till()
            if get_entity_type() == None:
                plant(ent)
            while get_water() < min_water:
                use_item(Items.Water)
            while measure() != cactus_size:
                while not can_harvest():
                    change_hat(Hats.Brown_Hat)
                    change_hat(Hats.Straw_Hat)
                harvest()
                plant(ent)
    print("!")

def main():
    cols, rows = 4, 8
    w = get_world_size() // cols
    h = get_world_size() // rows
    while True:
        utils.move_to(0, 0)
        drones = []
        for i in range(cols):
            for j in range(rows):
                utils.move_to(i*w, j*h)
                if i == cols-1 and j == rows-1:
                    break
                drone = spawn_drone(same)
                drones.append(drone)
        same()
        for drone in drones:
            wait_for(drone)
        harvest()

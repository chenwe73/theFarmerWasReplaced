import utils

min_water = 0.9

def main():
    ent = Entities.Sunflower
    min_petal, max_petal = 7, 15
    x, y = get_pos_x(), get_pos_y()
    for i in range(5):
        for j in range(2):
            utils.move_to(x+i, y+j)
            if get_ground_type() == Grounds.Grassland:
                till()
            if get_entity_type() == None:
                plant(ent)
                while measure() > min_petal:
                    harvest()
                    plant(ent)
    utils.move_to(x, y)
    if get_ground_type() == Grounds.Grassland:
        till()
    while True:
        if can_harvest():
            harvest()
        if get_entity_type() == None:
            plant(ent)
        while get_water() < min_water:
            use_item(Items.Water)
        if num_items(Items.Fertilizer) > 0 and num_items(Items.Weird_Substance) > 0:
            use_item(Items.Fertilizer)
            use_item(Items.Weird_Substance)

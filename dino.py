import utils

size = 32

def main():
    set_world_size(size)
    while True:
        utils.move_to(0, 0)
        change_hat(Hats.Dinosaur_Hat)
        x, y = measure()
        quick_print(x,y)
        while True:
            for i in range(1, size-1, 2):
                utils.move_to(0, i)
                utils.move_to(size-2, i)
                utils.move_to(size-2, i+1)
                utils.move_to(0, i+1)
            utils.move_to(0, size-1)
            utils.move_to(size-1, size-1)
            utils.move_to(size-1, 0)
            utils.move_to(0, 0)
            if utils.is_stuck():
                change_hat(Hats.Straw_Hat)
                break

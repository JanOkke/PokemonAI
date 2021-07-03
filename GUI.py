import os

def draw_battle_back(pos: [int, int], terrain: str = "Cave"):
    if terrain == "Cave":
        img = pygame.image.load(os.getcwd() + "\\Graphics\\Battlebacks\\battlebgCave.png")
        #img.resize(SIZE)
        screen.blit(img, pos)


def draw_battler(pokemon_id: int, pos: [int, int], front_sprite=False, back_sprite=False):
    while len(str(pokemon_id)) < 3:
        pokemon_id = "0" + str(pokemon_id)
    if front_sprite:
        img = pygame.image.load(os.getcwd() + "\\Graphics\\Battlers\\" + str(pokemon_id) + ".png")
        screen.blit(img, pos)


def MoveChooser(moves):
    pass  # TODO

if __name__ == '__main__':

    import pygame
    SIZE = (800, 600)

    pygame.init()
    display = pygame.display
    screen = display.set_mode(SIZE)
    running = True
    fps = 60
    clock = pygame.time.Clock()
    draw_battle_back([0, 0])
    draw_battler(150, [100, 100], True, False)
    display.flip()
    while running:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

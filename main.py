import pygame, sys, pymunk

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0, 9.8)  # wind and gravity


def create_apple(space):
    body = pymunk.Body(1, 10, body_type=pymunk.Body.DYNAMIC)  # mass, inertia, body type
    body.position = (400, 0)
    shape = pymunk.Circle(body, 80)
    space.add(body, shape)
    return shape


def create_static(space):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)  # mass, inertia, body type
    body.position = (400, 400)
    shape = pymunk.Circle(body, 80)
    space.add(body, shape)
    return shape


def draw_apples(apples):
    for apple in apples:
        pos_x = int(apple.body.position.x)
        pos_y = int(apple.body.position.y)
        pygame.draw.circle(screen, (255, 0, 0), (pos_x, pos_y), 80)


def draw_static(statics):
    for static in statics:
        pos_x = int(static.body.position.x)
        pos_y = int(static.body.position.y)
        pygame.draw.circle(screen, (255, 255, 0), (pos_x, pos_y), 80)


def draw():
    screen.fill((217, 217, 217))
    draw_apples(apples)
    draw_static(statics)
    space.step(1 / 50)
    pygame.display.update()
    clock.tick(120)


apples = [create_apple(space)]
statics = [create_static(space)]
while True:
    draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                apples[0].body.apply_impulse_at_local_point((0, -40))

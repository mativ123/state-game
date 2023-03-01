import pygame

def aspect_scale(img, size: list[float]):
    w = 0
    h = 0
    if size[0] == 0 and size[1] == 0:
        raise Exception("begge kan ikke være 0")
    elif size[0] == 0:
        h = size[1]
        w = img.get_width() * (size[1] / img.get_height())
        return pygame.transform.scale(img, (w, h))
    elif size[1] == 0:
        w = size[0]
        h = img.get_height() * (size[0] / img.get_width())
        return pygame.transform.scale(img, (w, h))
    else:
        return "din mor"

def andInp(event, walkSpeed):
    speed = [0, 0]
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            speed[0] = walkSpeed
        if event.key == pygame.K_LEFT:
            speed[0] = -walkSpeed
        if event.key == pygame.K_DOWN:
            speed[1] = walkSpeed
        if event.key == pygame.K_UP:
            speed[1] = -walkSpeed
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            speed[0] = 0
        if event.key == pygame.K_LEFT:
            speed[0] = 0
        if event.key == pygame.K_DOWN:
            speed[1] = 0
        if event.key == pygame.K_UP:
            speed[1] = 0
    return speed

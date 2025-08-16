import pygame
pygame.init()
SCREEN_WIDTH,SCREEN_HEIGHT=500,500
display_surface=pygame.dispaly.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.dispaly.set_caption('adding imageand background image')
background_image=pygame.transform.scale(
    pygame.image.load('background.png').convrt(),
    (SCREEN_WIDTH,SCREEN_HEIGHT))
penguin_image=pygame.transform.scale(
    pygame.image.load('hello penguin.png').convert_alpha(),(200,200)
penguin_react=penguin_imge.get_react(center=(SCREEN_WIDTH//2,
                                             SCREEN_HEIGHT//2-30 ))
text=pygame.font.Font(None,360).render('hello world ',True,
                                        pygame.coor('black'))
text_rect=text.get_rect(center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2+110)))
def game_loop():
    clock



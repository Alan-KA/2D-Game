import pygame
from sys import exit
from random import randint

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface=text_font.render(f'Score: {current_time}',False,(64,64,64))#specify content, ,color
    score_rectangle = score_surface.get_rect(center = (400,50))
    screen.blit(score_surface,score_rectangle)
    return current_time

def obstacle_movement(obstacle_list):
  if obstacle_list:
    for obstacle_rect in obstacle_list:
      obstacle_rect.x -= 5

      screen.blit(snail_surface,obstacle_rect)

    obstacle_list=[obstacle for obstacle in obstacle_list if obstacle.x > -100]

    return obstacle_list
  else:
    return []

def collisions(player,obstacles):
  if obstacles:
    for obstacle_rect in obstacles:
      if player.colliderect(obstacle_rect):return False
  return True

def player_animation():
  global player_surface,player_index

  if player_rectangle.bottom < 300:
    player_surface = player_jump
  else:
    player_index += 0.1
    if player_index >= len(player_walk):
      player_index = 0
    player_surface = player_walk[int(player_index)]

pygame.init()
screen = pygame.display.set_mode((800,400))#setting screen width and height
pygame.display.set_caption('Runner')

#set constant speed to the game
clock = pygame.time.Clock()
#adding a text
text_font=pygame.font.Font('font/Pixeltype.ttf',40)#specify text style and size
game_active = False

sky_surface = pygame.image.load('Assets/Sky.png').convert()
ground_surface=pygame.image.load('Assets/ground.png').convert()

#score_surface=test_font.render('my first game',False,(64,64,64))#specify content, ,color
#score_rectangle = score_surface.get_rect(center = (400,50))

#obstacles
snail_surface=pygame.image.load('Assets/snail1.png').convert_alpha()
snail_rectangle= snail_surface.get_rect(bottomright=(700,300))



obstacle_rect_list = []
#snail_x_pos = 600
player_walk_1=pygame.image.load('Assets/player_walk_1.png').convert_alpha()
player_walk_2=pygame.image.load('Assets/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1,player_walk_2]
player_index = 0
player_jump = pygame.image.load('Assets/jump.png').convert_alpha()

player_surface = player_walk[player_index]

player_rectangle=player_surface.get_rect(midbottom = (80,300))

player_gravity = 0
#intro screen
player_stand = pygame.image.load('Assets/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (400,200))

game_name = text_font.render('Runner',False,(111,196,169))
game_name_rect = game_name.get_rect(center = (400,80))

game_message = text_font.render('Press space to run',False,(111,196,169))
game_message_rect = game_message.get_rect(center = (400,340))

#Timer
obstacle_timer= pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500)

start_time = 0
score = 0

while True:
    

    for event in pygame.event.get():
       if event.type == pygame.QUIT:
          pygame.quit()
          exit()

       if game_active:
           if event.type == pygame.MOUSEBUTTONDOWN and player_rectangle.bottom >=300:
            if player_rectangle.collidepoint(event.pos):
               player_gravity = -20
      



           if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rectangle.bottom >=300:
              player_gravity = -20

       else:
          if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
           game_active = True
           snail_rectangle.left  = 800
           start_time =  int(pygame.time.get_ticks() / 1000)

       if event.type == obstacle_timer and game_active:
         obstacle_rect_list.append(snail_surface.get_rect(bottomright=(randint(900,1100),300)))
   

     
 
    if  game_active:
         screen.blit(sky_surface,(0,0)) 
         screen.blit(ground_surface,(0,300))

         score = display_score()

         #pygame.draw.rect(screen,'#c0e8ec',score_rectangle)
         #pygame.draw.rect(screen,'#c0e8ec',score_rectangle,10)
    
         #screen.blit(score_surface,score_rectangle) 
        #  display_score() 
        #  snail_rectangle.x -= 4
        #  if snail_rectangle.right <=0: snail_rectangle.left =800

        #  screen.blit(snail_surface,snail_rectangle)
    #player_rectangle.left += 1

    #player
         player_gravity += 1 
         player_rectangle.y += player_gravity 
         if player_rectangle.bottom >=300:
          player_rectangle.bottom = 300  
          player_animation()
         screen.blit(player_surface,player_rectangle)

    #obstacle movement
         obstacle_rect_list = obstacle_movement(obstacle_rect_list)

    #collision 
         game_active=collisions(player_rectangle,obstacle_rect_list)

        #  if snail_rectangle.colliderect(player_rectangle):
        #   game_active = False
    else:
      screen.fill((94,129,162))
      screen.blit(player_stand,player_stand_rect)

      obstacle_rect_list.clear()
      player_rectangle.midbottom = (80,300)
      player_gravity = 0



      score_message = text_font.render(f'Your score : {score}',False,(111,196,169))
      score_message_rect = score_message.get_rect(center = (400,330))

      screen.blit(game_name,game_name_rect)
      if score == 0:
        screen.blit(game_message,game_message_rect)
      else:
        screen.blit(score_message,score_message_rect)


  

    


    pygame.display.update()
    clock.tick(60)
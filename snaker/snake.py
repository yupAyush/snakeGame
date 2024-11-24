
import pygame,sys,random
from pygame.math import Vector2
class Snake:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.di = Vector2(1,0)
        self.new_block = False

        self.head_up = pygame.image.load('/home/Ayush/Desktop/snaker/head_u.png').convert_alpha()
        self.head_down = pygame.image.load('/home/Ayush/Desktop/snaker/head_d.png').convert_alpha()
        self.head_right = pygame.image.load('/home/Ayush/Desktop/snaker/head_r.png').convert_alpha()
        self.head_left = pygame.image.load('/home/Ayush/Desktop/snaker/head_l.png').convert_alpha()

        self.tail_up = pygame.image.load('/home/Ayush/Desktop/snaker/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('/home/Ayush/Desktop/snaker/tail_down.png').convert_alpha()
        self.tail_right= pygame.image.load('/home/Ayush/Desktop/snaker/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('/home/Ayush/Desktop/snaker/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('/home/Ayush/Desktop/snaker/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('/home/Ayush/Desktop/snaker/body_horizontal.png').convert_alpha()

        self.body_bl = pygame.image.load('/home/Ayush/Desktop/snaker/body_bl.png').convert_alpha()
        self.body_br = pygame.image.load('/home/Ayush/Desktop/snaker/body_br.png').convert_alpha()
        self.body_tl = pygame.image.load('/home/Ayush/Desktop/snaker/body_tl.png').convert_alpha()
        self.body_tr = pygame.image.load('/home/Ayush/Desktop/snaker/body_tr.png').convert_alpha()

        self.crunch_sound = pygame.mixer.Sound('/home/Ayush/Desktop/snaker/sound.mp3')
    
    def update_head_graphic(self):
        head_relation = self.body[1]-self.body[0]
        if head_relation == Vector2(1,0): self.head = self.head_left
        elif head_relation == Vector2(-1,0): self.head = self.head_right
        elif head_relation == Vector2(0,1): self.head = self.head_up
        elif head_relation == Vector2(0,-1): self.head = self.head_down

    def draw_snake(self):
        self.update_head_graphic()
        self.update_tail_graphics()
        for index,block in enumerate(self.body):
           x_pos = int(block.x*c_size)
           y_pos=  int(block.y*c_size)
           block_rect = pygame.Rect(x_pos,y_pos,c_size,c_size)

           if index == 0:
              screen.blit(self.head_right,block_rect)
           elif index == len(self.body)-1:
              screen.blit(self.tail,block_rect)
           else:
              previous_block = self.body[index+1]-block
              next_block = self.body[index-1]-block
              if previous_block.x == next_block.x:
                  screen.blit(self.body_vertical,block_rect)
              elif previous_block.y== next_block.y:
                  screen.blit(self.body_horizontal,block_rect)   
              else:
                  if previous_block.x == -1 and next_block.y== -1 or   previous_block.y == -1 and next_block.x== -1:
                     screen.blit(self.body_tl,block_rect) 
                  elif previous_block.x == -1 and next_block.y== 1 or   previous_block.y == 1 and next_block.x== -1:
                     screen.blit(self.body_bl,block_rect) 
                  elif previous_block.x == 1 and next_block.y== -1 or   previous_block.y == -1 and next_block.x== 1:
                     screen.blit(self.body_tr,block_rect)  
                  elif previous_block.x == 1 and next_block.y== 1 or   previous_block.y == 1 and next_block.x== 1:
                     screen.blit(self.body_br,block_rect)  
              
    
    
    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1,0): self.tail = self.tail_left
        elif tail_relation == Vector2(-1,0): self.tail = self.tail_right
        elif tail_relation == Vector2(0,1): self.tail = self.tail_up
        elif tail_relation == Vector2(0,-1): self.tail = self.tail_down      

		

    def move_snake(self):
        if self.new_block == True:
          body_copy= self.body[:]
          body_copy.insert(0,body_copy[0]+ self.di)
          self.body = body_copy[:]
          self.new_block = False
        else:
             body_copy= self.body[:-1]
        body_copy.insert(0,body_copy[0]+ self.di)
        self.body = body_copy[:]
    def add_block(self):
        self.new_block = True
    def play_sound(self):
        self.crunch_sound.play() 
    def reset(self):
        self.body=[Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.di = Vector2(0,0)       

                             
class Fruit:
    def __init__(self):
       self.randomize()
       self.x = random.randint(0,c_number-1)
       self.y = random.randint(0,c_number-1)
       self.p = Vector2(self.x,self.y)
    def draw_fruit(self):
       fruit_rect =pygame.Rect(int(self.p.x*c_size),int(self.p.y*c_size),c_size,c_size)
       screen.blit(b1,fruit_rect)
    def randomize(self):

       self.x = random.randint(0,c_number-1)
       self.y = random.randint(0,c_number-1)
       self.p = Vector2(self.x,self.y)  
    

class Main:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()
    def update(self):    
        self.snake.move_snake()
        self.check_collison()
        self.check_fail()
    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()
    def check_collison(self):
        if self.fruit.p == self.snake.body[0]:   
            self.fruit.randomize() 
            self.snake.add_block()
            self.snake.play_sound()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x< c_number or not 0 <= self.snake.body[0].y< c_number:
            self.game_over()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()    
    def game_over(self):  
            pygame.quit()
            sys.exit()
    def draw_grass(self):
        grass_color = (167,209,61)
        for row in range(c_number):
            if row% 2 == 0:
              for col in range(c_number):
                if col % 2== 0:
                 grass_rect = pygame.Rect(col*c_size,row*c_size,c_size,c_size)
                 pygame.draw.rect(screen,grass_color,grass_rect) 
            else:
              for col in range(c_number):
                if col % 2!= 0:
                 grass_rect = pygame.Rect(col*c_size,row*c_size,c_size,c_size)
                 pygame.draw.rect(screen,grass_color,grass_rect)  
    def draw_score(self):
        score_text = str(len(self.snake.body)-3)
        score_surface = game_font.render(score_text,True,(56,74,12))
        score_x = int(c_size*c_number - 60)
        score_y = int(c_size*c_number - 40)
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        screen.blit(score_surface,score_rect)        


pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
c_size=30
c_number = 20
screen= pygame.display.set_mode((c_size*c_number,c_size*c_number))
clock = pygame.time.Clock()
banana = pygame.image.load('/home/Ayush/Desktop/snaker/1.png').convert_alpha()
b1 =pygame.transform.scale(banana,(35,35))
game_font = pygame.font.Font(None,25)

Screen_update = pygame.USEREVENT
pygame.time.set_timer(Screen_update,150)

main_game = Main()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == Screen_update:
            main_game.update()   
        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_UP:
                if main_game.snake.di.y !=1:
                 main_game.snake.di = Vector2(0,-1)    
            if event.key == pygame.K_DOWN:
                if main_game.snake.di.y !=-1:
                 main_game.snake.di = Vector2(0,1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.di.x !=1:
                 main_game.snake.di = Vector2(-1,0)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.di.x !=-1:
                 main_game.snake.di = Vector2(1,0)           
                           
          
    screen.fill((175,215,70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)
         
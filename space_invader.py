from tkinter import *
from timeit import default_timer as timer
window=Tk()
window.title("Space Invader")
window.geometry("600x800")
game = Canvas(window, width=600, height=800, background='black')
game.pack()
player_sprite = PhotoImage(file="player.png")
bullet_sprite = PhotoImage(file="bullet.png")
enemy_sprite = PhotoImage(file="alien.png")
player = game.create_image(300, 700, anchor=NW, image=player_sprite)
level = 0
player_life = 30
playing = False
game_over_text = ""
x_vel = 0
y_vel = 0
shot_load = 0

def main_menu():
    playing = True

def options_menu():
    print("options")
    
def pause():
    print("pause")

def game_over():
    global playing
    playing = False
    game.delete("all")
    game.update()
    while playing == False:
        text1 = game.create_text(300, 200, text = 'GAME OVER', font = ('Helvetica', 40, 'bold'), justify = 'center', fill='red')
        text2 = game.create_text(300, 300, text = game_over_text, font = ('Helvetica', 20, 'bold'), justify = 'center', fill='red')
        game.update()

def enemy_creation():
    global level
    for h in range (level):
        for l in range (2*level):
            game.create_image(120+50*l,120+50*h, anchor=NW, image=enemy_sprite, tag="enemy")
            game.update()
    enemy_move()

def collision():
    global player_life, game_over_text
    enemies = game.find_withtag("enemy")
    for i in enemies:
        e = game.coords(i)
        colliding = game.find_overlapping(e[0],e[1],e[0]+32,e[1]+24)
        if len(colliding)>1:
            for j in colliding:
                if j == player:
                    player_life = player_life - 10
                    game.delete("life_bar")
                    game.create_text(100, 100, text = "HP: "+ str(player_life), font = ('Helvetica', 20, 'bold'), justify = 'center', fill='red',tag="life_bar")
                    if player_life<=0:
                        game_over_text = "The aliens destroyed your ship!"
                        game_over()
                else:
                    game.delete(j)
        if game.find_overlapping(0,795,600,800):
            game_over_text = "The aliens escaped!"
            game_over()
            
def enemy_move():
    global level
    if player_life>0:
        if game.find_withtag("enemy"):
                game.move("enemy",0,10)
                collision()
                game.update()
                game.after(700-(100*level),enemy_move)
        else:
            game.delete("bullet")
            game.update()
            level = level + 1
            if level <= 1:
                level_text1 = "Ready? Go!"
                level_text2 = ""
            else:
                level_text1 = "Level " + str(level-1) + " completed!"
                level_text2 = "Level " + str(level) + " loading..."
            game.create_text(300, 200, text = level_text1, font = ('Helvetica', 40, 'bold'), justify = 'center', fill='yellow', tag="text")
            game.create_text(300, 300, text = level_text2, font = ('Helvetica', 20, 'bold'), justify = 'center', fill='yellow', tag="text")
            game.update()
            game.after(2000)
            game.delete("text")
            enemy_creation()
enemy_move()

        
def player_move():
    game.move(player,x_vel,y_vel)

def shot():
    global shot_load
    shot_load = 1
    game.after(700,shot)
    
def key_pressed(event):
    global x_vel, y_vel,shot_load
    touche = event.keysym
    c = game.coords(player)
    if touche == "Right" and c[0]<790:
        x_vel = 10
    if touche == "Left" and c[0]>10:
        x_vel = -10
    if touche == "Up" and c[1]>400:
        y_vel = -10
    if touche == "Down" and c[1]<750:
        y_vel =  10
    if touche == "space" and shot_load == 1:
        shot_load = 0
        game.create_image(c[0]+12,c[1]-12, anchor=NW, image=bullet_sprite, tag="bullet")
        game.update()
    player_move()
        
def key_released(event):
    global x_vel,y_vel
    touche = event.keysym
    if touche == "Right":
        x_vel = 0
    if touche == "Left":
        x_vel = 0
    if touche == "Up":
        y_vel = 0
    if touche == "Down":
        y_vel =  0

def shot_move():
    game.move("bullet",0,-10)
    game.update()
    collision()
    game.after(70,shot_move)

game.create_text(100, 100, text = "HP: "+ str(player_life), font = ('Helvetica', 20, 'bold'), justify = 'center', fill='red',tag="life_bar")
shot()
shot_move()
game.focus_set()
game.bind("<KeyPress>", key_pressed)
game.bind("<KeyRelease>", key_released)
window.mainloop()

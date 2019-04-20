from tkinter import *
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

def player_shot(event):
    touche = event.keysym
    game.create_image(c[0]+12,c[1]-12, anchor=NW, image=bullet_sprite, tag="bullet")
    game.update()
        
def player_right(event):
     c = game.coords(player)
     if c[0]<600:
        game.move(player,10,0)
        game.update()

def player_left(event):
     c = game.coords(player)
     if c[0]<600:
        game.move(player,10,0)
        game.update()

def player_up(event):
     c = game.coords(player)
     if c[0]<600:
        game.move(player,10,0)
        game.update()

def player_down(event):
     c = game.coords(player)
     if c[0]<600:
        game.move(player,10,0)
        game.update()

        
def shot_move():
    game.move("bullet",0,-10)
    game.update()
    collision()
    game.after(80,shot_move)

game.create_text(100, 100, text = "HP: "+ str(player_life), font = ('Helvetica', 20, 'bold'), justify = 'center', fill='red',tag="life_bar")
shot_move()
game.focus_set()
game.bind_all("<KeyPress-space>", player_shot)
game.bind_all("<KeyPress-right>", player_right)
game.bind_all("<KeyPress-left>", player_left)
game.bind_all("<KeyPress-up>", player_up)
game.bind_all("<KeyPress-down>", player_down)
window.mainloop()

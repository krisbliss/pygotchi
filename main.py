from time import sleep
import tkinter as tk
from canvas_values import *
# from gotchi.gotchi_class import Gotchi
from gotchi.gotchi_classes import Baby, Teen, Adult
from food.food_classes import Cookie
from time import *

def main():
    
    # player sets name in terminal
    pygotchiname = input("What is your Pygotchi's name? ")

    # root tkinter object
    root = tk.Tk();
    root.title(f"{pygotchiname}'s World")

    # container canvas for main background, name, and nested gotchi_canvas
    main_canvas = tk.Canvas(root,width=CANVAS_WIDTH, height=CANVAS_HEIGHT,bg='lightblue')
    main_canvas.pack()

    gotchi_canvas = tk.Canvas(root, width=GOTCHI_BOX_WIDTH, height=GOTCHI_BOX_HEIGHT, bg='lightgray', highlightthickness=2, highlightbackground='black')
    main_canvas.create_window(GOTCHI_BOX_X, GOTCHI_BOX_Y, window=gotchi_canvas)

    status_text = main_canvas.create_text(20,20, anchor="nw", font=("Arial", 30), fill='black',text=f"{pygotchiname} is a baby!")

    # create food object
    cookie = Cookie(main_canvas)

    # make cookie clickable 
    main_canvas.tag_bind(cookie.cookie_base,"<Button-1>", print("clicked")) # <Button-1> == left mouse click
  
    # preload all the pigotchi life stages
    baby = Baby(gotchi_canvas)
    teen = Teen(gotchi_canvas)
    adult = Adult(gotchi_canvas)
    
    
    # gets current time for interval comparisons to be done for pygotchi life stages
    START_TIME = time()
    def game_loop():
        elapsed_time = time() - START_TIME

        # single var to denote which active gotchi to animate
        active_gotchi = None

        if elapsed_time < 10:
            active_gotchi = baby
            baby.show()
            teen.hide()
            adult.hide()

        elif elapsed_time < 20:
            main_canvas.itemconfig(status_text, text=f"{pygotchiname} is now a teenager!")
            active_gotchi = teen
            baby.hide()
            teen.show()
            adult.hide()

        elif elapsed_time < 30:
            main_canvas.itemconfig(status_text, text=f"{pygotchiname} is an adult!")
            active_gotchi = adult
            baby.hide()
            teen.hide()
            adult.show()

        else:
            main_canvas.itemconfig(status_text, text=f"Great job raising {pygotchiname}!")
            return
        
        # run animcaiton function for currently active_gotchi
        active_gotchi.animate()

        # update screen to reflect gotchi movment every 300 millieseconds
        root.after(300,game_loop)
            
    game_loop()
    root.mainloop()

if __name__ == '__main__':
    main()

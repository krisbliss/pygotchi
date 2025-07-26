from time import sleep
import tkinter as tk
from canvas_values import *
# from gotchi.gotchi_class import Gotchi
from gotchi.gotchi_classes import Baby, Teen, Adult
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
        

        active_gotchi.animate()

        # update screen to reflect gotchi movment every 300 millieseconds
        root.after(300,game_loop)
            
    # # init current_time to start processing pygotchi life stages loop
    # current_time = time()
    # while (current_time - START_TIME) < 300:
    #     current_time = time() # recalculate current time each time the program loops
    #     sleep(1) # puts a pause so there is a brief break before the next animate loop
    #
    #     if (current_time - START_TIME) < 30: # sets 30 seconds for this animation loop
    #
    #         #hide irrelevant evolutions
    #         teengotchi.hidegotchi()
    #         adultgotchi.hidegotchi()
    #
    #         # animate current evolution
    #         babygotchi.animate(gotchibox)
    #
    #     elif (current_time - START_TIME) <= 120:
    #         canvas.delete(gotchistate) 
    #         gotchistate = canvas.create_text(20, 20, anchor = "w", font = "Arial 30", text = f"{pygotchiname} is now a teenager!")
    #         # hide irrelevant evolutions
    #         babygotchi.hidegotchi()
    #         adultgotchi.hidegotchi()
    #
    #         # show and animate current evolution
    #         teengotchi.showgotchi()
    #         teengotchi.animate(gotchibox)
    #
    #     else:
    #         # hide irrelevant evolutions
    #         babygotchi.hidegotchi()
    #         teengotchi.hidegotchi()
    #
    #         # show and animate current evolution
    #         adultgotchi.showgotchi()
    #         adultgotchi.animate(gotchibox)
    #
    #         canvas.delete(gotchistate)
    #         gotchistate = canvas.create_text(20, 20, anchor = "w", font = "Arial 30", text = f"{pygotchiname} has grown into an adult!")
    #
    #     canvas.update() # runs every time it loops, updates the canvas every time it changes
    #
    # canvas.delete(gotchistate)
    # gotchistate = canvas.create_text(20, 20, anchor = "w", font = "Arial 30", text = f"Great job taking such good care of {pygotchiname}!")
    
    # root.update()
    game_loop()
    root.mainloop()

if __name__ == '__main__':
    main()

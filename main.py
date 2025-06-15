from time import sleep
from graphics import Canvas
import random
from time import *

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 800
START_TIME = time()

GOTCHI_BOX_X0 = CANVAS_WIDTH / 8 # start at first 8th
GOTCHI_BOX_Y0 = 300
GOTCHI_BOX_X1 =  (CANVAS_WIDTH * 7) / 8  # end at last 8th
GOTCHI_BOX_Y1 = CANVAS_HEIGHT - 100

class gotchi():
    def __init__(self, canvas, type):
        # universal constants for each type of PyGothci
        self.canvas = canvas
        self.body_center_x = CANVAS_WIDTH // 2 # CENTER x coordinate
        self.body_center_y = (CANVAS_HEIGHT * 2)/3 # y about 2/3 of the way DOWN
        self.type = type
        self.direction = "right" # for animate()
        self.idle_reset = 0 # for animate()

     #if statement to determine body shape and size
        if self.type == "baby":
            self.body_size = 100
        elif self.type == "teen":
            self.body_size = 150
        elif self.type == "adult":
            self.body_size = 120

        # below calls the functions created to stack in order and make each shape
        self.createbody()
        self.createeyes()
        self.createmouth()

    def randomcolor(self):
        random_color = random.randint(1,3)
        if random_color == 1:
            self.color = "blue"
        elif random_color == 2:
            self.color = "red"
        elif random_color == 3:
            self.color = "green"

    def createbody(self):
        self.randomcolor()

        # values for specific Pygotchi bodies
        self.body_start_x = self.body_center_x - self.body_size/2
        self.body_start_y = self.body_center_y - self.body_size/2
        body_end_x = self.body_center_x + self.body_size/2
        body_end_y = self.body_center_y + self.body_size/2

        # for triangle adult
        body_top_x = self.body_center_x
        body_top_y = self.body_center_y - 100

        if self.type == "baby":
            self.body = self.canvas.create_oval(self.body_start_x, self.body_start_y, body_end_x, body_end_y, self.color)
        elif self.type == "teen":
            self.body = self.canvas.create_rectangle(self.body_start_x, self.body_start_y, body_end_x, body_end_y, self.color)
        elif self.type == "adult": # triangle, using polygons
            #self.body = self.canvas.create_polygon(100, 500, 300, 500, 200, 100, fill=self.color)
            self.body = self.canvas.create_polygon(self.body_start_x - self.body_size/2,self.body_start_y+self.body_size,body_end_x+self.body_size/2,body_end_y,body_top_x,body_top_y, fill='green', outline = 'black')
            
    def createeyes(self):
        # values for calculating eye positions and dimensions
        eye_radius = 10
        x_eyes_offset = 35
        y_eyes_offset = 30

        # left eye position
        left_eye_x = self.body_center_x - x_eyes_offset
        left_eye_y = self.body_center_y - y_eyes_offset

        # right eye position
        right_eye_x = self.body_center_x + x_eyes_offset
        right_eye_y = self.body_center_y - y_eyes_offset

        # create eyes
        self.left_eye = self.canvas.create_oval(left_eye_x - eye_radius, left_eye_y - eye_radius, left_eye_x + eye_radius, left_eye_y + eye_radius, 'black')
        self.right_eye = self.canvas.create_oval(right_eye_x - eye_radius, right_eye_y - eye_radius, right_eye_x + eye_radius, right_eye_y + eye_radius, 'black')


    def createmouth(self):
        # mouth dimensions
        mouth_width = 35
        mouth_height = 20

        # curve start
        mouth_x_start = self.body_center_x - mouth_width // 2   # double divide returns whole integer number
        mouth_y_start = self.body_center_y + 5

        # curve end
        mouth_x_end = self.body_center_x + mouth_width // 2
        mouth_y_end = mouth_y_start + mouth_height

        # create mouth object
        self.mouth = self.canvas.create_arc(mouth_x_start, mouth_y_start, mouth_x_end, mouth_y_end, start=180, extent=180, style="arc", width=3,outline='black',fill='black')


    def animate(self, gotchibox):
        coordinates = self.canvas.bbox(self.body) # bbox is a function within canvas that returns coordinates, in this case, for the body of the pygotchi which is the largest object printed on screen
        # list, coordinates at index - [x0, y0, x1, y1]

        gotchibox = self.canvas.bbox(gotchibox)

        # set animation to move down and right
        if self.direction == "right" and self.idle_reset == 0: # when starting, this is always TRUE because direction is set as right to start
            if coordinates[2] <= gotchibox[2] - 30 and coordinates[3] <= gotchibox[3]- 30: # checks coordinates against canvas max with offset 30 to make sure shape stays within canvas
                # move function that will move each created object right 10, down 10
                self.canvas.move(self.body, 10, 10)
                self.canvas.move(self.left_eye, 10, 10)
                self.canvas.move(self.right_eye, 10, 10)
                self.canvas.move(self.mouth, 10, 10)
            else:
                self.direction = "left" # flips direction/preset it left for the next run
                self.idle_reset = 1 # used to reset center

        # set animation to move down and left
        elif self.direction == "left" and self.idle_reset == 0:
            if coordinates[0] >= gotchibox[0] - 30 and coordinates[3] <= gotchibox[3] - 30:
                self.canvas.move(self.body, -10, 10) # opposite direction as above, but same offsets - left (-)10, down 10
                self.canvas.move(self.left_eye, -10, 10)
                self.canvas.move(self.right_eye, -10, 10)
                self.canvas.move(self.mouth, -10, 10)

            else:
                self.direction = "right" #flip back to the right
                self.idle_reset = 1

        # resent animation center
        elif self.idle_reset == 1:
            # if object is BELOW starting point, start moving up and in the appropriate direction
            if coordinates[1] >= self.body_start_y and self.direction == "left":
                  self.canvas.move(self.body, -10, -10) # basically undoes original right + down
                  self.canvas.move(self.left_eye, -10, -10)
                  self.canvas.move(self.right_eye, -10, -10)
                  self.canvas.move(self.mouth, -10, -10)

            elif coordinates[1] >= self.body_start_y and self.direction == "right":
                  self.canvas.move(self.body, 10, -10) # flips above left + down
                  self.canvas.move(self.left_eye, 10, -10)
                  self.canvas.move(self.right_eye, 10, -10)
                  self.canvas.move(self.mouth, 10, -10)  
            else:
                self.idle_reset = 0

    def hidegotchi(self): # function to hide gotchi using this function
        self.canvas.itemconfig(self.body, state="hidden")
        self.canvas.itemconfig(self.left_eye, state="hidden")
        self.canvas.itemconfig(self.right_eye, state="hidden")
        self.canvas.itemconfig(self.mouth, state="hidden")

    def showgotchi(self): # unhides gotchi with this function
        self.canvas.itemconfig(self.body, state="normal")
        self.canvas.itemconfig(self.left_eye, state="normal")
        self.canvas.itemconfig(self.right_eye, state="normal")
        self.canvas.itemconfig(self.mouth, state="normal")




def main():
    pygotchiname = input("What is your Pygotchi's name? ")
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT, pygotchiname)
    background = canvas.create_rectangle(0,0, CANVAS_WIDTH, CANVAS_HEIGHT, "white")
    gotchibox = canvas.create_rectangle(GOTCHI_BOX_X0, GOTCHI_BOX_Y0, GOTCHI_BOX_X1, GOTCHI_BOX_Y1, "lightgray") # create a box for pygotchi to bounce in
   # for future: figure out why outline isn't working
    current_time = time()
    gotchistate = canvas.create_text(20, 20, anchor = "w", font = "Arial 30", text = f"{pygotchiname} is currently a baby!")
    babygotchi = gotchi(canvas, "baby")
    teengotchi = gotchi(canvas, "teen")
    adultgotchi = gotchi(canvas, "adult")

    while (current_time - START_TIME) < 300:
        current_time = time() # recalculate current time each time the program loops
        sleep(1) # puts a pause so there is a brief break before the next animate loop

        if (current_time - START_TIME) < 30: # sets 30 seconds for this animation loop

            #hide irrelevant evolutions
            teengotchi.hidegotchi()
            adultgotchi.hidegotchi()

            # animate current evolution
            babygotchi.animate(gotchibox)

        elif (current_time - START_TIME) <= 120:
            canvas.delete(gotchistate) 
            gotchistate = canvas.create_text(20, 20, anchor = "w", font = "Arial 30", text = f"{pygotchiname} is now a teenager!")
            # hide irrelevant evolutions
            babygotchi.hidegotchi()
            adultgotchi.hidegotchi()

            # show and animate current evolution
            teengotchi.showgotchi()
            teengotchi.animate(gotchibox)

        else:
            # hide irrelevant evolutions
            babygotchi.hidegotchi()
            teengotchi.hidegotchi()

            # show and animate current evolution
            adultgotchi.showgotchi()
            adultgotchi.animate(gotchibox)

            canvas.delete(gotchistate)
            gotchistate = canvas.create_text(20, 20, anchor = "w", font = "Arial 30", text = f"{pygotchiname} has grown into an adult!")

        canvas.update() # runs every time it loops, updates the canvas every time it changes

    canvas.delete(gotchistate)
    gotchistate = canvas.create_text(20, 20, anchor = "w", font = "Arial 30", text = f"Great job taking such good care of {pygotchiname}!")

    canvas.mainloop()


""""  
    while current_time - START_TIME < 10:
        current_time = time.time()
        print(current_time - START_TIME)
        canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, 'white')  # this creates a white bg
        babygotchi(canvas)
        canvas.update()

    while current_time - START_TIME < 30:
        current_time = time.time()
        print(current_time - START_TIME)
        canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, 'white')  # this creates a white bg
        teengotchi(canvas)
        canvas.update()

    while current_time - START_TIME < 60:
        current_time = time.time()
        print(current_time - START_TIME)
        canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, 'white')  # this creates a white bg
        adultgotchi(canvas)
        canvas.update()

    print("Your tama died bro")
"""


"""""
        if current_time - START_TIME < 10:
            babygotchi(canvas)
        elif current_time - START_TIME < 35 and current_time - START_TIME > 10:
            teengotchi(canvas)
        else:
            adultgotchi(canvas)
        """
if __name__ == '__main__':
    main()
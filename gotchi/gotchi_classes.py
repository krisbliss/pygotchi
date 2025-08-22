from .life_stages.babies.Test_Baby import TestBabyFeatures
from .life_stages.teens.Test_Teen import TestTeenFeatures
from .life_stages.adults.Test_Adult import TestAdultFeatures
import random

# --- Base Class --- #
class Gotchi:
    """
    Grandparent class that handles the following logic:
        1) Animation / movement
        2) obtaining the root.canvas and dimensions
        3) holding parts[] list
    """
    def __init__(self,canvas):
        self.canvas = canvas
        self.parts = [] #init empty list
        self.tag = ""

        # get canvas dimensions
        self.canvas_width = int(self.canvas.cget("width"))
        self.canvas_height = int(self.canvas.cget("height"))

        # Velocity & direciton for movement animation
        self.dx = random.choice([-2,2])
        self.dy = random.choice([-2,2])

        # Universal center for gotchi body spawn
        self.center_x = self.canvas_width /2
        self.center_y = self.canvas_height /2


    # used by child classes to append 
    def add_part(self,part_id):
        self.parts.append(part_id)
    
    
    # used in main() function's game_loop() to disaplay gotchi movement 
    def animate(self):
        
        # guard clause to stop program if parts[] list is empty
        if not self.parts:
            return
        
        # canvas.bbox will collect coordinate info for main body 
        # Note: assuming main body is first element added to list
        x0,y0,x1,y1 = self.canvas.bbox(self.parts[0])
        
        # check if any of main body's coordinates collide with edges of canvas
        if x0 <= 0 or x1 >= self.canvas_width:
            self.dx *= -1 # invert the direciton of dx upon collision  

        if y0 <= 0 or y1 >= self.canvas_height:
            self.dy *= -1 # invert the direciton of dy upon collision  

        # move ALL parts of gotchi as single unit
        #for part in self.parts:
        #    self.canvas.move(part, self.dx, self. dy)
        
        self.canvas.move(self.tag, self.dx, self. dy)

    
    def hide(self):
        #for part in self.parts:
        #   self.canvas.itemconfig(part,state='hidden')
        self.canvas.itemconfig(self.tag,state='hidden')

    def show(self):
        #for part in self.parts:
        #    self.canvas.itemconfig(part,state='normal')
        self.canvas.itemconfig(self.tag,state='normal')


# --- Baby --- #
class Baby(Gotchi):

    def __init__(self,canvas):
        super().__init__(canvas) # create instance of Gotchi (aka parent class) as part of current class
        self.body_size = 100
        self.tag = "baby"

        # static features class for now, will update this in future to be modular in accepting another type of class file to represent different variants of baby gotchi
        features = TestBabyFeatures(self.canvas, self.center_x, self.center_y, self.body_size, self.tag)
        for part in features.get_all_feature_ids():
            self.add_part(part)

        # after creation, start in hidden state 
        self.hide()

# --- Teen --- #
class Teen(Gotchi):
    def __init__(self,canvas):
        super().__init__(canvas)
        self.body_size = 150
        self.tag = "teen"

        # function to store array of objects that make up gotchi's features
        features = TestTeenFeatures(self.canvas, self.center_x, self.center_y, self.body_size, self.tag)
        for part in features.get_all_feature_ids():
            self.add_part(part)

        # start in hidden state
        self.hide()

# --- Adult --- #
class Adult(Gotchi):
    def __init__(self,canvas):
        super().__init__(canvas)
        self.body_size = 300
        self.tag = "adult"
        
        # function to store array of objects that make up gotchi's features
        features = TestAdultFeatures(self.canvas, self.center_x, self.center_y, self.body_size, self.tag)
        for part in features.get_all_feature_ids():
            self.add_part(part)

        # start in hidden state
        self.hide()

from time import *
import math

class Food:

    """
    Food class to handel the following:
        1) Hold object list of shapes to display on canvas
        2) Handel clickable reactions from user
        3) Help provide Happiness update for gotchi depending on subclass 
    """

    def __init__(self,canvas):
        # static values for any circular food item
        self.size = 75
        self.radius = self.size/2

        # universal
        self.canvas = canvas
        self.parts = []

        # place holder for callback passed in from active_gotchi (handled in main.py)
        self.onClick_callback = None  #NOTE: May need to make this a list of functions in the future to handle opening and closing of mouth interlaced with cookie biting animation 

        # place holder for internal object instance of food subclass
        self.display_food = None
        
        # place holder for relavent tag to be set in subclass
        self.tag = ""
        
        # get canvas dimensions
        self.canvas_width = int(self.canvas.cget("width"))
        self.canvas_height = int(self.canvas.cget("height"))
        self.canvas_bg = self.canvas.cget("bg")


    def _handle_onClick_food_animation(self, event):
        # initiates callback set from active_gotchi and handles displaying animation of cookie being eaten
        if self.onClick_callback:
            self.onClick_callback()
            
            # if parts list is empty, then object has not yet been drawn
            if not self.display_food.parts:
                self.display_food._draw()
            
            # on second click, take bite
            else:
                self.display_food._bite_animation()
                print("bite taken")

        else:
            print("No callback from gotchi_clases has been set")
        

    def set_onClick_fun(self,onClick_callback):
        # attach externally passed function to the object's self.onClick, this will get called 
        self.onClick_callback = onClick_callback


    # function to make the object a button, only needed for 
    def _set_button_tags(self):

        # change tag to be unique from 
        self.tag = f"{self.tag}_button"
        for part in self.parts:
            self.canvas.itemconfig(part,tags=self.tag)

        # Binding fuction from tkinter to handle when user left clicks on objects with self.tag associated with it to run the _handle_onClick function
        self.canvas.tag_bind(self.tag,"<Button-1>",self._handle_onClick_food_animation)


    def _bite_animation(self):
        
        # Hide original food drawing 
        bitten_tag = f"{self.tag}_bitten"
        
        # draw out the bite marks that overlap original food object image
        num_teeth_marks = 4
        bite_angle_start = 0
        bite_angle_span = 90
        bite_radius = self.radius * 0.4

        for i in range(num_teeth_marks):
            angle_rad = math.radians(bite_angle_start + (i * bite_angle_span / (num_teeth_marks - 1)))
            
            bite_center_x = self.center_x + (self.radius * 0.8) * math.cos(angle_rad)
            bite_center_y = self.center_y - (self.radius * 0.8) * math.sin(angle_rad)
            
            bx0, by0 = bite_center_x - bite_radius, bite_center_y - bite_radius
            bx1, by1 = bite_center_x + bite_radius, bite_center_y + bite_radius
            # Create the bite mark and immediately tag it with the new bitten_tag
            self.canvas.create_oval(bx0, by0, bx1, by1, fill=self.canvas_bg, outline="", tags=bitten_tag)

        # --- Retag the original food parts to share the new tag ---
        # This groups the original food and the bite marks together.
        self.canvas.itemconfig(self.tag, tags=bitten_tag)

  
class Cookie(Food):

    """
        Constructor to create button or food item for gotchi to eat based on passed in values
        1)  Button if passed in values for button_location_x and y
        2)  Food item for animation of gotchi eating if no other args are passed in
    """

    def __init__(self, canvas, gotchi_canvas=None, onClick_callback=None, button_location_x = (1/4), button_location_y = (1/4)):
        super().__init__(canvas)
        self.center_x = self.canvas_width * button_location_x
        self.center_y = self.canvas_height * button_location_y
        self.tag = "cookie"

        # set object as button and create dummy object to display on gotchi_canvas when clicked
        if gotchi_canvas:
            self.display_food = Cookie(gotchi_canvas)
            self.onClick_callback = onClick_callback
            self._draw()
            self._set_button_tags()

    def _draw(self):
        # create local coordiates to determin center of cookie and chips
        x0 = self.center_x - self.radius
        y0 = self.center_y - self.radius
        x1 = self.center_x + self.radius
        y1 = self.center_y + self.radius

        cookie_base = self.canvas.create_oval(
            x0,y0,x1,y1,
            fill="#D2B48C",
            outline = "black",
            width = 2,
            tags = self.tag 
        )
        
        # keep track of cookie base and chips for this exact instance of cookie
        # we can use this for touching / changing items for this instance of cookie even if other instances with the same tag exsit already
        self.parts.append(cookie_base)
 
        # static position for chips to be drawn on cookie
        chip_positions = [
            (0.5, 0.2),
            (-0.4, 0.6),
            (-0.6, -0.3),
            (0.1, -0.5),
            (0.0, 0.0) # Center chip
        ]
        
        # loop through all positions and create chip objects
        for pos_x, pos_y in chip_positions:
            # Calculate the absolute position for each chip
            chip_x = self.center_x + pos_x * self.radius
            chip_y = self.center_y + pos_y * self.radius
            
            chip_radius = self.size / 15
            chip_x0 = chip_x - chip_radius
            chip_y0 = chip_y - chip_radius
            chip_x1 = chip_x + chip_radius
            chip_y1 = chip_y + chip_radius

            # append each chip object into parts array
            self.parts.append(self.canvas.create_oval(
                    chip_x0, chip_y0, chip_x1, chip_y1,
                    fill="#3E2723",
                    outline="",
                    tags = self.tag
                )
            )

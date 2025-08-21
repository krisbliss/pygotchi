
class Food:

    """
    Food class to handel the following:
        1) Hold object list of shapes to display on canvas
        2) Handel clickable reactions from user
        3) Help provide Happiness update for gotchi depending on subclass 
    """

    def __init__(self,canvas):
        self.canvas = canvas
        
        # get canvas dimensions
        self.canvas_width = int(self.canvas.cget("width"))
        self.canvas_height = int(self.canvas.cget("height"))
        
        # store list of objects to be displayed
        self.parts = []

    def _onClick(self):
        pass

    def _BiteAnimiation(self):
        pass


class Cookie(Food):
    
    def __init__(self,canvas,onClick=None):
        super().__init__(canvas)
        self.center_x = self.canvas_width * (6/8)
        self.center_y = self.canvas_height * (1/8)
        self.size = 75
        self.radius = self.size/2
        self.onClick_callback = onClick # pass a callback function (if none presented, default to None)
        self.tag = "cookie"

        # create local coordiates to determin center of cookie and chips
        x0 = self.center_x - self.radius
        y0 = self.center_y - self.radius
        x1 = self.center_x + self.radius
        y1 = self.center_y + self.radius

        self.cookie_base = self.canvas.create_oval(
            x0,y0,x1,y1,
            fill="#D2B48C",
            outline = "black",
            width = 2,
            tags = self.tag 
        )
        
        #shapes = [] # insert class hear that returns list of shapes that make up cookie
        chip_positions = [
            (0.5, 0.2),
            (-0.4, 0.6),
            (-0.6, -0.3),
            (0.1, -0.5),
            (0.0, 0.0) # Center chip
        ]
        
        for pos_x, pos_y in chip_positions:
            # Calculate the absolute position for each chip
            chip_x = self.center_x + pos_x * self.radius
            chip_y = self.center_y + pos_y * self.radius
            
            chip_radius = self.size / 15
            chip_x0 = chip_x - chip_radius
            chip_y0 = chip_y - chip_radius
            chip_x1 = chip_x + chip_radius
            chip_y1 = chip_y + chip_radius

            self.canvas.create_oval(
                chip_x0, chip_y0, chip_x1, chip_y1,
                fill="#3E2723",
                outline="",
                tags = self.tag
            )
        
        # Binding fuction from tkinter to handle when user left clicks on objects with self.tag associated with it to run the _handle_onClick function
        self.canvas.tag_bind(self.tag, "<Button-1>",self._handle_onClick)

    def _handle_onClick(self,event):
    
        # Will plan to use callback feature in future to pass happieness level functions from gotchi_classes.py 
        #
        #if self.onClick_callback:
        #    self.onClick_callback()
        #
        # for right now, just testing with print output
        print("clicked")



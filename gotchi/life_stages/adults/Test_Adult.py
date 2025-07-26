from ...parts.eyes.Test_Eyes import Eyes
from ...parts.mouth.Test_Mouth import Mouth
import random

class TestAdultFeatures:
    # Defines the specific features for an adult.
    def __init__(self, canvas, center_x, center_y, body_size):

        #define specific body style features unique to this gotchi
        color = random.choice(["steelblue", "firebrick", "seagreen"])
        # Coordinates for a triangle body
        x0 = center_x - body_size / 2
        y1 = center_y + body_size / 2
        top_x = center_x
        y0 = center_y - body_size / 2
        x1 = center_x + body_size / 2
        points = [x0, y1, top_x, y0, x1, y1]

        # creates single list item to ALLWAYS be appened first
        self.body_id = [canvas.create_polygon(points, fill=color, outline="black", width=2)]
 

        # use universal or modular eyes / mouth 
        # each item is list item
        self.eyes = Eyes(canvas, center_x, center_y, x_offset=body_size/3, y_offset=body_size/3, radius=8)
        self.mouth = Mouth(canvas, center_x, center_y, width=body_size/4, height_offset=body_size/4)
    
    # returns list of concatinated lists
    def get_all_feature_ids(self):
        return self.body_id + self.eyes.get_ids() + self.mouth.get_ids()


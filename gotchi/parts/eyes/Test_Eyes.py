class Eyes():
    # Creates a pair of eyes.
    def __init__(self, canvas, tag, center_x, center_y, x_offset, y_offset, radius=10):
        self.canvas = canvas

        # Left eye
        lx = center_x - x_offset
        ly = center_y - y_offset
        self.left_eye = self.canvas.create_oval(
            lx - radius, 
            ly - radius, 
            lx + radius, 
            ly + radius, 
            fill='black', 
            outline='black',
            tags = tag
        )
        
        # Right eye
        rx = center_x + x_offset
        ry = center_y - y_offset
        self.right_eye = self.canvas.create_oval(
            rx - radius, 
            ry - radius, 
            rx + radius, 
            ry + radius, 
            fill='black', 
            outline='black',
            tags = tag
        )

    def get_ids(self):
        return [self.left_eye, self.right_eye]



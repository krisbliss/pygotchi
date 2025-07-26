class Mouth():
    # generic mouth.
    def __init__(self, canvas, center_x, center_y, width, height_offset):
        self.canvas = canvas
        x0 = center_x - width / 2
        y0 = center_y + height_offset
        x1 = center_x + width / 2
        y1 = y0 + 15 # Mouth height
        self.mouth = self.canvas.create_arc(x0, y0, x1, y1, start=180, extent=180, style="arc", width=3, outline='black')

    def get_ids(self):
        return [self.mouth]



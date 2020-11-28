class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def __str__(self):
        linestr = str()
        
        classname = str(type(self).__name__)
        linestr = linestr + classname + "(width=" + str(self.width) + ", height=" + str(self.height) + ")"

        return linestr

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return float(self.width * self.height)

    def get_perimeter(self):
        return float(2 * (self.width + self.height))

    def get_diagonal(self):
        return float( (self.width ** 2 + self.height ** 2) ** 0.5)

    def get_picture(self):
        lines = str()

        if self.width > 50 or self.height > 50:
            lines = "Too big for picture."
        else:
            for i in range(0, self.height):
                lines = lines + "*" * self.width
                lines = lines + "\n"

        return lines

    def get_amount_inside(self, shapecomp):

        widthdiv = self.width // shapecomp.width
        heightdiv = self.height // shapecomp.height
        if widthdiv == 0 or widthdiv == 0 : return 0
        else:
            return widthdiv * heightdiv
        


class Square(Rectangle):
    def __init__(self, width):
        super().__init__(width, width)

    def __str__(self):
        linestr = str()
        
        classname = str(type(self).__name__)
        
        linestr = linestr + classname + "(side=" + str(self.width) + ")"

        return linestr

    def set_side(self, width):
        self.set_width(width)
        self.set_height(width)
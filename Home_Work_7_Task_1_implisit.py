import math as m


def triangle_area():
    """
    This function calculate an area
    of triangle
    Input parameters:
    Output: float
    """
    while 1:
        try:
            triangle_side = float(input(
                "Insert side of triangle:"
                ))
            triangle_height = float(input(
                "Insert triangle height taken from that side:"
                ))
            return round(0.5 * triangle_side * triangle_height, 2)
        except ValueError:
            print("Try again!")


def rectangle_area():
    """
    This function calculate
    an area of rectangle
    Input parameters:
    Output: float
    """

    while 1:
        try:
            rectangle_lenght = float(input(
                "Insert rectangle lenght:"
                ))
            rectangle_height = float(input(
                "Insert rectangle height:"
                ))
            return round(rectangle_lenght*rectangle_height, 2)
        except ValueError:
            print("Try again!")



def circle_area():
    """
    This function calculate an area
    of circle
    Input parameters:
    Output: float
    """

    while 1:
        try:
            circle_radius = float(input(
                "Enter circle radius:"
                ))
            return round(m.pi * m.pow(circle_radius,2), 2)
        except ValueError:
            print("Try again!")



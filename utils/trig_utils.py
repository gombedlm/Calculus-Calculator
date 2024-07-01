import math

def round_angle(angle):
    """Rounds the given angle to the nearest whole number."""
    return round(angle)

def calculate_height(side_c, angle_A):
    """Calculates the height of the triangle."""
    return side_c * math.sin(math.radians(angle_A))

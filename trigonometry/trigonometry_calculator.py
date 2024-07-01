import math
import sys
from utils.trig_utils import round_angle, calculate_height

class TrigonometryCalculator:
    """A class to perform trigonometric calculations on triangles."""
    def __init__(self):
        pass

    def calculate_triangle(self, angle_A=None, side_a=None, side_c=None):
        """
        Calculates the properties of a triangle given an angle and two sides.
        
        Args:
            angle_A (float): The angle opposite side_a in degrees.
            side_a (float): The length of side a.
            side_c (float): The length of side c.
        """
        if angle_A is not None and side_a is not None and side_c is not None:
            if side_a >= side_c:
                print("1 solution exists")
            else:
                print("Calculating the height")
                height = calculate_height(side_c, angle_A)
                print(f"Height: {height:.2f}")
                height = round(height)
                print(f"Rounded Height: {height}")

                solutions = self.determine_solutions(height, side_a, side_c)

                if solutions == 0:
                    sys.exit()
                elif solutions == 1:
                    self.calculate_one_solution(angle_A, side_a, side_c)
                elif solutions == 2:
                    self.calculate_two_solutions(angle_A, side_a, side_c)
        else:
            print("Please provide valid inputs for angle A, side a, and side c")

    def determine_solutions(self, height, side_a, side_c):
        """
        Determines the number of solutions for the triangle.
        
        Args:
            height (float): The height of the triangle.
            side_a (float): The length of side a.
            side_c (float): The length of side c.
        
        Returns:
            int: The number of solutions (0, 1, or 2).
        """
        if side_a < height:
            print("No solution exists")
            return 0
        elif side_a == height:
            print("1 solution exists")
            return 1
        elif height < side_a < side_c:
            print("2 solutions exist")
            return 2

    def calculate_one_solution(self, angle_A, side_a, side_c):
        """
        Calculates and prints the properties of the triangle for one solution.
        
        Args:
            angle_A (float): The angle opposite side_a in degrees.
            side_a (float): The length of side a.
            side_c (float): The length of side c.
        """
        angle_C = round_angle(math.degrees(math.asin(side_a * math.sin(math.radians(angle_A)) / side_c)))
        angle_B = 180 - (angle_A + angle_C)
        side_b = (side_a * math.sin(math.radians(angle_B))) / math.sin(math.radians(angle_A))

        print(f"<A: {angle_A}°, side a: {side_a}")
        print(f"<B: {angle_B}°, side b: {side_b:.2f}")
        print(f"<C: {angle_C}°, side c: {side_c}")

    def calculate_two_solutions(self, angle_A, side_a, side_c):
        """
        Calculates and prints the properties of the triangle for two solutions.
        
        Args:
            angle_A (float): The angle opposite side_a in degrees.
            side_a (float): The length of side a.
            side_c (float): The length of side c.
        """
        angle_C = round_angle(math.degrees(math.asin(side_a * math.sin(math.radians(angle_A)) / side_c)))
        angle_B = 180 - (angle_A + angle_C)
        side_b = (side_a * math.sin(math.radians(angle_B))) / math.sin(math.radians(angle_A))

        angle_A2 = angle_A
        side_a2 = side_a
        side_c2 = side_c

        angle_B2 = 180 - angle_B
        angle_C2 = 180 - (angle_A2 + angle_B2)

        print(f"Solution 1:")
        print(f"<A: {angle_A}°, side a: {side_a}")
        print(f"<B: {angle_B}°, side b: {side_b:.2f}")
        print(f"<C: {angle_C}°, side c: {side_c}")

        print(f"Solution 2:")
        print(f"<A: {angle_A2}°, side a: {side_a2}")
        print(f"<B: {angle_B2}°, side b: {side_b:.2f}")
        print(f"<C: {angle_C2}°, side c: {side_c2}")

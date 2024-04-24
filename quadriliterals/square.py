import math

from quadriliterals.rectangle import Rectangle


class Square(Rectangle):

    def _calculate_area(self):
        return self.sides[0] ** 2

    def _calculate_diagonals(self):
        return (math.sqrt(2) * self.sides[0],)

    def _calculate_angles(self):
        # All angles in a square are 90 degrees
        return (90, 90, 90, 90)
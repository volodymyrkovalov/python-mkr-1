import math

from quadriliterals.quadriliteral import Quadrilateral


class Trapezium(Quadrilateral):
    def _calculate_height(self):
        # Example height calculation, assuming we know the coordinates exactly for simplicity
        # This is a placeholder logic; actual computation needs more precise vertex positions
        return math.fabs(self.vertices[2][1] - self.vertices[0][1])

    def _calculate_area(self):
        # Calculate base lengths directly in the area calculation
        base1 = self.sides[0]
        base2 = self.sides[2]
        height = math.fabs(self.vertices[2][1] - self.vertices[0][1])  # Simple vertical height calculation
        return 0.5 * (base1 + base2) * height

    def _calculate_diagonals(self):
        # Diagonal calculations could be more complex based on exact coordinates
        diagonal1 = math.sqrt((self.vertices[0][0] - self.vertices[2][0])**2 + (self.vertices[0][1] - self.vertices[2][1])**2)
        diagonal2 = math.sqrt((self.vertices[1][0] - self.vertices[3][0])**2 + (self.vertices[1][1] - self.vertices[3][1])**2)
        return (diagonal1, diagonal2)

    def _calculate_angles(self):
        angles = []
        n = len(self.vertices)
        for i in range(n):
            # Get the vectors for the sides meeting at vertex i
            v1 = (self.vertices[i - 1][0] - self.vertices[i][0], self.vertices[i - 1][1] - self.vertices[i][1])
            v2 = (
            self.vertices[(i + 1) % n][0] - self.vertices[i][0], self.vertices[(i + 1) % n][1] - self.vertices[i][1])
            # Calculate angle using the dot product formula
            angle = self._angle_between(v1, v2)
            angles.append(angle)
        return tuple(angles)

    def _angle_between(self, v1, v2):
        # Compute the dot product of v1 and v2
        dot = v1[0] * v2[0] + v1[1] * v2[1]
        # Compute the magnitudes of v1 and v2
        mag1 = math.sqrt(v1[0]**2 + v1[1]**2)
        mag2 = math.sqrt(v2[0]**2 + v2[1]**2)
        # Compute the cosine of the angle
        cos_angle = dot / (mag1 * mag2)
        # Avoid precision issues at boundaries
        cos_angle = max(min(cos_angle, 1), -1)
        # Compute the angle in degrees
        angle = math.degrees(math.acos(cos_angle))
        return angle
from quadriliterals.trapezium import Trapezium


class RightTrapezium(Trapezium):
    def __init__(self, vertices):
        super().__init__(vertices)
        # Angles specific to right trapezium where two angles are 90 degrees
        self.angles = (90, 90, self.angles[2], self.angles[3])  # Assuming the right angles at vertices 0 and 1

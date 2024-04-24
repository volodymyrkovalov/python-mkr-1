from abc import ABC, abstractmethod
import uuid
import math


# Base class for all quadrilaterals
class Quadrilateral(ABC):
    def __init__(self, vertices):
        self.vertices = vertices  # (x, y) pairs
        self.type = self.__class__.__name__
        self.id = uuid.uuid4()
        self.sides = self._calculate_sides()
        self.perimeter = self._calculate_perimeter()
        self.area = self._calculate_area()
        self.diagonals = self._calculate_diagonals()
        self.angles = self._calculate_angles()

    def _distance(self, point1, point2):
        return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

    def _calculate_sides(self):
        a = self._distance(self.vertices[0], self.vertices[1])
        b = self._distance(self.vertices[1], self.vertices[2])
        c = self._distance(self.vertices[2], self.vertices[3])
        d = self._distance(self.vertices[3], self.vertices[0])
        return a, b, c, d

    def _calculate_perimeter(self):
        return sum(self.sides)

    @abstractmethod
    def _calculate_area(self):
        pass

    @abstractmethod
    def _calculate_diagonals(self):
        pass

    @abstractmethod
    def _calculate_angles(self):
        pass

    def get_sides(self):
        return self.sides

    def get_perimeter(self):
        return self.perimeter

    def get_area(self):
        return self.area

    def get_diagonals(self):
        return self.diagonals

    def get_angles(self):
        return self.angles

    @classmethod
    def get_subtype_list(cls):
        return cls.__subclasses__()

    @classmethod
    def get_supertype_list(cls):
        return cls.__bases__

    @classmethod
    def is_type(cls, instance):
        return isinstance(instance, cls)

    def __eq__(self, other):
        if self.area == other.area and self.perimeter == other.perimeter:
            return True
        return False

    def __lt__(self, other):
        if self.area < other.area or (self.area == other.area and self.perimeter < other.perimeter):
            return True
        return False

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

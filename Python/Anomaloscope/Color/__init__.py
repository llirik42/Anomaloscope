from math import sqrt

from dataclasses import dataclass


__all__ = ['Color']


@dataclass
class Color:
    red: float
    green: float
    blue: float

    def __init__(self, red: float, green: float, blue: float) -> None:
        self.red = max(red, 0)
        self.green = max(green, 0)
        self.blue = max(blue, 0)

    @property
    def rounded_repr(self) -> str:
        rounded_red = int(round(self.red))
        rounded_green = int(round(self.green))
        rounded_blue = int(round(self.blue))

        return f'({rounded_red} {rounded_green} {rounded_blue})'

    def __sub__(self, other) -> float:
        return sqrt((self.red-other.red)**2 + (self.green-other.green)**2 + (self.blue-other.blue)**2)

    def __repr__(self) -> str:
        return f'({self.red} {self.green} {self.blue})'

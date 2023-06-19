from dataclasses import dataclass
from typing import List

from config import NUMBER_OF_SORTED_COLORS_TO_PRINT
from Color import Color
from SerialReader import SerialData


__all__ = ['DataAnalyzer', 'AnalyzedData']


@dataclass
class AnalyzedData:
    x: List[float]=None
    y: List[float]=None

    number_of_cases: int=-1
    sorted_elements: List[Color]=None


class DataAnalyzer:
    __serial_data: SerialData
    __analyzed_data: AnalyzedData=AnalyzedData()
    __number_of_colors_to_print: int

    def __init__(self, serial_data: SerialData, number_of_colors_to_print: int=NUMBER_OF_SORTED_COLORS_TO_PRINT):
        self.__serial_data = serial_data

        self.__number_of_colors_to_print = number_of_colors_to_print

    @property
    def analyzed_data(self) -> AnalyzedData:
        return self.__analyzed_data

    def analyze(self) -> None:
        self.__calculate_x_y()
        self.__sort_iterating_colors()

        for i in range(self.__number_of_colors_to_print):
            print(self.__analyzed_data.sorted_elements)

    def __calculate_x_y(self) -> None:
        self.__analyzed_data.x = []
        self.__analyzed_data.y = []

        for index in range(self.__serial_data.number_of_cases):
            self.__analyzed_data.x.append(index + 1)
            self.__analyzed_data.y.append(self.__serial_data.elements[index].difference)

    def __sort_iterating_colors(self) -> None:
        self.__analyzed_data.sorted_elements = sorted(self.__serial_data.elements, key=lambda element: element.difference)

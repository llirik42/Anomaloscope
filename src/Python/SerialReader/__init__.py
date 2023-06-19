from dataclasses import dataclass
from serial.serialwin32 import Serial
from typing import List

from Color import Color
from config import DISPLAY_PROGRESS


__all__ = ['SerialReader', 'SerialData', 'ReaderSettings']


@dataclass
class ReaderSettings:
    serial: Serial
    display_progress: bool=DISPLAY_PROGRESS


@dataclass
class SerialDataElement:
    iterating_color: Color
    sensor_color: Color
    difference: float


@dataclass
class SerialData:
    number_of_cases: int=-1
    target_color: Color=None
    elements: List[SerialDataElement]=None


class SerialReader:
    __settings: ReaderSettings
    __data: SerialData=SerialData()

    def __init__(self, settings: ReaderSettings):
        self.__settings = settings

    def read(self) -> None:
        self.__read_first_line_data()

        self.__read_main_data()

    @property
    def data(self) -> SerialData:
        return self.__data

    def __read_first_line_data(self) -> None:
        numbers_in_first_line = self.__numbers_in_cur_serial_line

        red = int(numbers_in_first_line[1])
        green = int(numbers_in_first_line[2])
        blue = 0

        self.__data.number_of_cases = int(numbers_in_first_line[0])
        self.__data.target_color = Color(red=red, green=green, blue=blue)

    def __display_progress(self, current_index: int) -> None:
        progress = 100 * current_index // self.__data.number_of_cases

        print(f'\r{progress}%', end='')

    def __read_main_data(self) -> None:
        self.data.elements = []

        for index in range(self.__data.number_of_cases):
            if self.__settings.display_progress:
                self.__display_progress(current_index=index)

            self.__data.elements.append(self.__element_in_cur_serial_line)

    @property
    def __element_in_cur_serial_line(self) -> SerialDataElement:
        numbers_in_current_line = self.__numbers_in_cur_serial_line

        cur_iterating_color = Color(
            red=255 * numbers_in_current_line[0],
            green=255 * numbers_in_current_line[1],
            blue=0
        )

        cur_sensor_color = Color(
            red=numbers_in_current_line[2],
            green=numbers_in_current_line[3],
            blue=0
        )

        cur_difference = self.__data.target_color - cur_sensor_color

        cur_element = SerialDataElement(
            iterating_color=cur_iterating_color,
            sensor_color=cur_sensor_color,
            difference=cur_difference
        )

        return cur_element

    @property
    def __cur_serial_line(self) -> str:
        return str(self.__settings.serial.readline())[2:-5]

    @property
    def __numbers_in_cur_serial_line(self) -> List[float]:
        return self.__get_numbers_in_line(self.__cur_serial_line)

    @staticmethod
    def __get_numbers_in_line(line: str) -> List[float]:
        numbers = []

        current_number = ''

        is_reading_of_number_started = False

        for current_char in line + ' ':
            # start of reading of number
            if current_char.isdigit() and not is_reading_of_number_started:
                is_reading_of_number_started = True

                current_number = ''

            # continuation of reading of number
            if is_reading_of_number_started:
                current_number += current_char

            # end of reading of number
            if not (current_char.isdigit() or current_char == '.') and is_reading_of_number_started:
                is_reading_of_number_started = False

                numbers.append(float(current_number))

        return numbers

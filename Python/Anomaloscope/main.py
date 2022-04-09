from pyqtgraph import QtCore
from pyqtgraph import QtGui
from sys import flags

from config import *
from SerialReader import ReaderSettings, SerialReader
from DataAnalyzer import DataAnalyzer
from PlotDrawer import DrawerSettings, PlotDrawer
from ArduinoSerial import get_arduino_serial


reader_settings = ReaderSettings(serial=get_arduino_serial(), display_progress=DISPLAY_PROGRESS)
reader = SerialReader(reader_settings)
reader.read()
serial_data = reader.data

analyzer = DataAnalyzer(serial_data=serial_data, number_of_colors_to_print=NUMBER_OF_SORTED_COLORS_TO_PRINT)
analyzer.analyze()
analyzed_data = analyzer.analyzed_data

drawer_settings = DrawerSettings(show_grid=SHOW_GRID, color=PLOT_COLOR, symbol=SYMBOL)
drawer = PlotDrawer(settings=drawer_settings, analyzed_data=analyzed_data)
drawer.draw()

if flags.interactive != 1 or not hasattr(QtCore, 'PYQT_VERSION'):
    QtGui.QGuiApplication.exec_()

from dataclasses import dataclass
from pyqtgraph import plot as window
from typing import Optional, List

from config import SYMBOL, SHOW_GRID, PLOT_COLOR
from DataAnalyzer import AnalyzedData


__all__ = ['DrawerSettings', 'PlotDrawer']


@dataclass
class DrawerSettings:
    show_grid: bool= SHOW_GRID,
    color: str=PLOT_COLOR
    symbol: Optional[str]=SYMBOL


class PlotDrawer:
    __settings: DrawerSettings
    __analyzed_data: AnalyzedData

    def __init__(self, settings: DrawerSettings, analyzed_data: AnalyzedData):
        self.__settings = settings

        self.__analyzed_data = analyzed_data

        self.__init_window()

    def __init_window(self) -> None:
        self.__window = window()
        self.__window.showGrid(x=self.__settings.show_grid, y=self.__settings.show_grid)

    def draw(self) -> None:
        self.draw_plot(
            x=self.__analyzed_data.x,
            y=self.__analyzed_data.y,
            color=self.__settings.color,
            symbol=self.__settings.symbol
        )

    def draw_plot(self, x: List[float], y: List[float], color: str, symbol: str) -> None:
        self.__window.plot(
            x=x,
            y=y,
            pen=color,
            symbol=symbol,
            symbolPen=color
        )

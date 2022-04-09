from serial.tools.list_ports import comports
from serial.serialwin32 import Serial
from typing import Optional

from config import BAUDRATE


__all__ = ['get_arduino_serial']


def get_arduino_serial() -> Optional[Serial]:
    port = get_arduino_port()

    if port is not None:
        return Serial(port=port, baudrate=BAUDRATE)

    return None


def get_arduino_port() -> Optional[str]:
    ports = comports()

    for port in ports:
        if "Arduino" in port.description:
            return port.device

    return None

#pragma once
#include <Arduino.h>

// �������� ������
class Color {   // ����� Color
public:
	Color(byte color = 5, byte bright = 30);
	void setColor(byte color);
	void setBright(byte bright);
	byte getColor();
	byte getBright();
private:
	byte _color;  // ���������� �����
	byte _bright; // ���������� �������
};
// ���������� �������
Color::Color(byte color = 5, byte bright = 30) { // �����������
	_color = color;   // ����������
	_bright = bright;
}
void Color::setColor(byte color) { _color = color; }
void Color::setBright(byte bright) { _bright = bright; }
byte Color::getColor() { return _color; }
byte Color::getBright() { return _bright; }
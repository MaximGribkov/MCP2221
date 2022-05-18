"""
-application icon license

(C) 2013 Yusuke Kamiyamane. All rights reserved.
<https://p.yusukekamiyamane.com/>

These icons are licensed under a Creative Commons
Attribution 3.0 License.
<http://creativecommons.org/licenses/by/3.0/>
Some icons by Yusuke Kamiyamane. Licensed under a Creative Commons Attribution 3.0 License.
"""
import sys

from PyMCP2221A import PyMCP2221A
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtCore import Qt


class my_app(QtWidgets.QWidget):
    def __init__(self):
        super(my_app, self).__init__()
        self.setWindowTitle('Панель управления')
        self.setWindowIcon(QtGui.QIcon('application-form.png'))
        self.layout_ = QtWidgets.QGridLayout()
        self.setLayout(self.layout_)
        """
--------------------------------------------------------------------------------------------------
        """
        self.btn_quit = QtWidgets.QPushButton('Закрыть')  # Кнопки / Button
        self.btn_write = QtWidgets.QPushButton('Запись')
        self.btn_read = QtWidgets.QPushButton('Чтение')
        self.btn_scan = QtWidgets.QPushButton('Скан')
        """
--------------------------------------------------------------------------------------------------
        """
        self.spin = QtWidgets.QSpinBox()  # Другие элементы / Other elements
        self.slider = QtWidgets.QSlider()
        self.label_1 = QtWidgets.QLabel('Введите адрес без "0х": ')
        self.label_2 = QtWidgets.QLabel('Введите число для записи: ')
        self.line_edit_address = QtWidgets.QLineEdit(self)
        self.label_3 = QtWidgets.QLabel('Вывод состояния: ')
        self.slider = QtWidgets.QSlider(Qt.Orientation.Horizontal)  # Горизонтальный вариант / Horizontal

        """
--------------------------------------------------------------------------------------------------
        """
        self.spin.setRange(0, 255)  # Настройка spin / settings spin
        self.spin.setSingleStep(1)
        self.value_of_spin = self.spin.valueChanged.connect(self.num_in_spin)
        """
--------------------------------------------------------------------------------------------------
        """
        self.slider.setRange(0, 255)  # Настройка slider / settings slider
        self.slider.setSingleStep(1)
        self.slider.valueChanged.connect(self.num_in_slider)
        """
--------------------------------------------------------------------------------------------------
        """
        self.layout_.addWidget(self.label_3, 5, 0, 1, 3)  # добавление на экран / add to window
        self.layout_.addWidget(self.spin, 2, 1)
        self.layout_.addWidget(self.slider, 1, 0, 1, 3)
        self.layout_.addWidget(self.label_1, 3, 0)
        self.layout_.addWidget(self.label_2, 2, 0)
        self.layout_.addWidget(self.line_edit_address, 3, 1)
        self.layout_.addWidget(self.btn_quit, 4, 2)
        self.layout_.addWidget(self.btn_write, 2, 2)
        self.layout_.addWidget(self.btn_read, 4, 1)
        self.layout_.addWidget(self.btn_scan, 4, 0)
        """
--------------------------------------------------------------------------------------------------
        """
        self.btn_quit.clicked.connect(app.quit)  # Команды кнопок / button commands
        self.btn_write.clicked.connect(self.write)
        self.btn_read.clicked.connect(self.read)
        self.btn_scan.clicked.connect(self.scan)
        """
--------------------------------------------------------------------------------------------------
        """

    def num_in_slider(self, p):
        self.spin.setValue(p)  # Установка числа в спинер / setting the number in the spin

    def num_in_spin(self, i):
        self.slider.setValue(i)  # Установка числа в слайдер / setting the number in the slider

    def read(self):
        try:
            mcp2221 = PyMCP2221A.PyMCP2221A()
            mcp2221.I2C_Init()
        except IndexError:  # Connection error
            self.label_3.setText('Вывод состояния: <html><head/><body><p><span ' +
                                 'style=\" font-size:10pt; color:#ff0000;\">' +
                                 'Ошибка чтения! Проверьте соединение с утройством</span></p></body></html>')
        else:
            try:
                hex_address_for_read = self.line_edit_address.displayText()  # Ввод адреса в hex формате
                # Entering an address in hex format
                dec_address_for_read = int(hex_address_for_read, 16)  # Перевод hex в десятичное число
                # Convert hex to decimal
                read_data = mcp2221.I2C_Read(dec_address_for_read, 2)[1]  # Значение без первого элемента
                # Value without first element
            except (ValueError, TypeError):  # Address error
                self.label_3.setText('Вывод состояния: <html><head/><body><p><span ' +
                                     'style=\" font-size:10pt; color:#ff0000;\">' +
                                     'Ошибка чтения! Введите корректный адрес устройства</span></p></body></html>')
            else:
                if read_data:
                    self.label_3.setText('Вывод состояния: значение на приборе {}'.format(read_data))

    def write(self):
        list_to_write = [0]  # Список для записи / record list
        try:
            mcp2221 = PyMCP2221A.PyMCP2221A()
            mcp2221.I2C_Init()
        except IndexError:  # Connection error
            self.label_3.setText('Вывод состояния: <html><head/><body><p><span ' +
                                 'style=\" font-size:10pt; color:#ff0000;\">' +
                                 'Ошибка записи! Проверьте соединение с утройством</span></p></body></html>')
        else:
            try:
                num_spin = self.spin.value()  # Берем число из spin для записи
                # Take a number from spin for writing
                list_to_write.append(num_spin)  # Добавляем в список для записи / add to list to write
                hex_address_for_write = self.line_edit_address.displayText()  # Ввод адреса в hex формате
                # Entering an address in hex format
                dec_address_for_write = int(hex_address_for_write, 16)  # Перевеод hex в десятичное число
                # Convert hex to decimal
                mcp2221.I2C_Write(dec_address_for_write, list_to_write)  # Функция записи / write function
            except (ValueError, TypeError):  # Address error
                self.label_3.setText('Вывод состояния: <html><head/><body><p><span ' +
                                     'style=\" font-size:10pt; color:#ff0000;\">' +
                                     'Ошибка записи! Введите корректный адрес устройства</span></p></body></html>')
            else:
                self.label_3.setText('Вывод состояния: запись выполнена, записано число: '
                                     + '{}'.format(list_to_write[1]))

    def scan(self):
        try:
            mcp2221 = PyMCP2221A.PyMCP2221A()
            mcp2221.I2C_Init()
        except IndexError:  # Connection error
            self.label_3.setText('Вывод состояния: <html><head/><body><p><span ' +
                                 'style=\" font-size:10pt; color:#ff0000;\">' +
                                 'Ошибка сканирования! Проверьте соединение с утройством</span></p></body></html>')
        else:
            for address in range(0x00, 0x7F):  # Ищем адрес в 7 битах / looking for an address in 7 bits
                if mcp2221.I2C_Read(address, 1) != -1:  # условие для поиска / search condition
                    self.label_3.setText('Вывод состояния: адрес устройства: 0x{:02X}'.format(address))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    window = my_app()
    window.setWindowIcon(QtGui.QIcon('application-form.png'))
    window.show()
    sys.exit(app.exec())

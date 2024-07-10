# mcp2221
Programm to work with MCP2221
A program for writing, reading from a chip and finding the address of the chip. Functionality implemented using PyQT6 and PyMCP2221A https://github.com/nonNoise/PyMCP2221A
A more detailed description of the work is in the datasheet https://supply24.online/doc/manual/Poluprovodniki/Mikroshimi/MICROCHIP-TECHNOLOGY/mcp2221.pdf

The program was tested in the following configuration: mcp2221 and one mcp4561 potentiometer.

The search for the chip address is performed in a 7-bit range, it is the same as 8-bit. For writing, a list is sent in which the first element is always 0. 
This is very important because the write will not be made. For more information, please see the datasheet.


Программа для записи, чтения с чипа и поиска адреса чипа. Функцианал реализиван с помощью PyQT6 и PyMCP2221A https://github.com/nonNoise/PyMCP2221A
Более подробное описание работы есть в даташите https://supply24.online/doc/manual/Poluprovodniki/Mikroshemi/MICROCHIP-TECHNOLOGY/mcp2221.pdf 

Программа тестировалась в такой конфигурации: mcp2221 и один потециометр mcp4561.

Поиск адреса чипа выполнияется в 7 битном диапазоне, он совпадает с 8 битным. 
Для записи оправляется список в котором первый элемент всегда равен 0. 
Это очень важно потому что запись не будет произведена. Для более подробной информации необходимо изуть даташит

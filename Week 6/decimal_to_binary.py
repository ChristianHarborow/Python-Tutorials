"""
    Decimal To Binary Converter

    Prints out a column of the decimal integers 0 to 127 alongside another column
    containing their 8-bit binary equivalents
"""

__author__ = "Christian Harborow"
__email__ = "u1856364@unimail.hud.ac.uk"
__date__ = "12/11/2018"

for decimal in range(0, 128):
    binary = bin(decimal)[2:]
    print(" " * (3-len(str(decimal))) + str(decimal), "0" * (8-len(binary)) + binary)

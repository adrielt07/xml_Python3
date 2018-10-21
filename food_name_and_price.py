#!/usr/bin/python3

'''
Printing the Menu and price
Format:
Food Name: Price
'''

import xml.etree.ElementTree as ET

tree = ET.parse('food.xml')
root = tree.getroot()

for child in root.iter('food'):
    print("{}: {}".format(child.find('name').text, child.find('price').text))

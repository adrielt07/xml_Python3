#!/usr/bin/python3

'''
Printing the Menu and price
Format:
Food Name: Price
'''

from defusedxml.ElementTree import parse

tree = parse('food.xml')
root = tree.getroot()

for child in root.iter('food'):
    print("{}: {}".format(child.find('name').text, child.find('price').text))

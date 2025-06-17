"""
Lab 13 Using Functions to Implement a Caesar Ciphers
"""
def getCipherKey():
    shiftAmount = input( "Please enter a key (whole number from 1-25): ")
    return shiftAmount
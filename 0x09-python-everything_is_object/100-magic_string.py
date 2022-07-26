#!/usr/bin/python3
"""
   module to create magic string
"""


def magic_string(list=[]):
    """
       magic_string - return a string "BestSchool" n times the number of the iteration
       How:
           create an empty list
           appending the string "BestSchool" to an empty list after each call of the func
           then add seperator ", " to the join the appended string to the established str
    """
    list.append("BestSchool")
    return ", ".join(list)

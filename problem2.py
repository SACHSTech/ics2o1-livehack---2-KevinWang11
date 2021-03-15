"""
-------------------------------------------------------------------------------
Name:   problem2.py
Purpose:  Write a program to have the user enter three lengths of sides and determine whether the figure is a triangle or not. . 

Author: Wang.K
 
Created:  24/02/2021
------------------------------------------------------------------------------
"""
# asks the user for the three sides of the triangle
side_1 = int(input("Please enter the value of side 1: "))
side_2 = int(input("Please enter the value of side 2: "))
side_3 = int(input("Please enter the value of side 3: "))

# calculates if the sides can form a triangle
if (side_1 + side_2 > side_3) and (side_2 + side_3 > side_1) and (side_1 + side_3 > side_2) :
  print("This is a triangle.")

# if the above is false, then the three sides cannot form a triangle.
else:
  print("This is not a triangle.")
    

"""
-------------------------------------------------------------------------------
Name:   problem1.py
Purpose:  Create a program that allows NASA's perseverance rover to determine what life form it is looking at based on the number of eyes and antennas it has. 

Author: Wang.K
 
Created:  24/02/2021
------------------------------------------------------------------------------
"""
#asks the user for the number of eyes and antennas.
eyes = int(input("How many eyes? "))
antennas = int(input("How many antennas? "))

#calculates what life form the user specified eyes and antennas will be. 
if antennas >= 3 and eyes <= 4:
  print("Life form detected: AudreyMartian")

elif antennas == 0 and eyes == 2:
  print("Life form detected: MattDamonMartian")

elif antennas <= 6 and eyes >= 2:
  print("Life form detected: MaxMartian")

  if antennas <= 2 and eyes <= 3:
      print("Life form detected: BrooklynMartian")

#prints error if the user input is not any of the Martians specified in the question.   
else:
  print("No life form detected.")
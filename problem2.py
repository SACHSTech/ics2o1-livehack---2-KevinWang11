side_1 = int(input("Please enter the value of side 1: "))
side_2 = int(input("Please enter the value of side 2: "))
side_3 = int(input("Please enter the value of side 3: "))

if (side_1 + side_2 > side_3) and (side_2 + side_3 > side_1) and (side_1 + side_3 > side_2) :
  print("This is a triangle.")
else:
  print("This is not a triangle.")
    

eyes = int(input("How many eyes? "))
antennas = int(input("How many antennas? "))

if antennas >= 3 and eyes <= 4:
  print("Life form detected: AudreyMartian")

elif antennas == 0 and eyes == 2:
  print("Life form detected: MattDamonMartian")

elif antennas <= 6 and eyes >= 2:
  print("Life form detected: MaxMartian")

  if antennas <= 2 and eyes <= 3:
      print("Life form detected: BrooklynMartian")
      
else:
  print("No life form detected.")
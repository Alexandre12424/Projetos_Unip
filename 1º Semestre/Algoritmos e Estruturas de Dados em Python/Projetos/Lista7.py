Firstlist = []
Secondlista = []
if Firstlist == Secondlist:
  print ("Both are equal")
else:
  print ("Both are not equal") 

if Firstlist is Secondlist:
  print ("Both variables are pointing to the same object")
else:
  print( "Both variables are not pointing to the same object")

Thirdlist = Firstlist

if Thirdlist is Secondlist:
  print ("Both are pointing to the same object")
else:
  print ("Both are not pointing to the same object")
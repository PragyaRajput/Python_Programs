for row in range(7):
  for col in range(5):
     if (row in {0,6}):
       print("*",end=' ')
     elif (row in {1}) and (col in {4}):
       print("*",end=' ')
     elif (row in {2}) and (col in {3}):
       print("*",end=' ')
     elif (row in {3}) and (col in {2}):
       print("*",end=' ')
     elif (row in {4}) and (col in {1}):
       print("*",end=' ')
     elif (row in {5}) and (col in {0}):
       print("*",end=' ')

     else:
       print(" ",end=' ')
  print()
       

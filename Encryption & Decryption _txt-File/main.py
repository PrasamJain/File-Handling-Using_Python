# we use open() function with w+ mode to open file and override the existing content to perform encryption and decryption.

f = open('text.txt','r')
data = f.read()
f.close()

x = int(input("Press \n1 for encrypt\n2 for decrypt\n"))
if x==1:
  f = open('text.txt','w+')
  s = ""
  for i in data:
    s = s + chr(ord(i)+65)
  f.write(s)
  print("Encrypted Successfully!!")
  f.close()
elif x==2:
  f = open('text.txt','w+')
  s = ""
  for i in data:
    s = s + chr(ord(i)-65)
  f.write(s)
  print("Decrypted Successfully!!")
  f.close()
else:
  print("invalid choice !!")

  
  
  
  
# ******** OUTPUT *********

# open('text.txt')
# File contains : Hello this is text.txt file for performing encryption and decryption.

# ENCRYPTED FILE : ¦­­°aµ©ª´aª´aµ¦¹µoµ¹µa§ª­¦a§°³a±¦³§°³®ª¯¨a¦¯¤³º±µª°¯a¢¯¥a¥¦¤³º±µª°¯o

# DECRYPTED FILE : Hello this is text.txt file for performing encryption and decryption.

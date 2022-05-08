# we use open() function with w+ mode to open file and override the existing content to perform encryption and decryption.

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

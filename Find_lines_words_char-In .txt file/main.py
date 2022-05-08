''' Program to read the file and Display the number of Lines , words and characters present in file.

 Example :  "Text.txt"
             Hello I'm Prasam Jain.
             I'am a programmer and Frontend Developer.

 OUTPUT : 
              lines :  2
              word :  10
              characters :  54 
'''

a = 0
b = 0
c = 0
file = open("text.txt","r")

for i in file:
  line = i.split()   #split in lines
  a+=1
  for word in line:   #split in words
    b+=1
    for char in word:   #split in character
      c+=1

file.close()

print("lines : ",a)
print("word : ",b)
print("characters : ",c)

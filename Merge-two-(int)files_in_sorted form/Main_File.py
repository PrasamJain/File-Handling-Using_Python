f1 = open("source1.txt",'r+')
f2 = open("source2.txt",'r+')

li1 = []
for i in f1:   #converting files into integer list
  li1.append(int(i))

li2 = []
for i in f2:
  li2.append(int(i))

li = []
li3 =(li1+li2)
while li3:    #apply sorting algorithm
    min = li3[0]  
    for x in li3: 
        if x < min:
            min = x
    li.append(str(min))
    li.append(" ")
    li3.remove(min)

target = open('target.txt','w+')

target.writelines(li)
target.close()

f1.close()
f2.close()

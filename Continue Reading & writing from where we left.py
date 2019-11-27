#Saving the last session in a text file
#And continue from where we left
import time
       
try:
       #Reading text file
       read_url = "text.txt"
       f = open(read_url, "r")
       lines = f.readlines()
       #print(lines[0])

       for i in range(int(lines[0]) , 60):
              print(str(i)+" -- "+" Seconds")
              f.close()
              g = open("text.txt","w")
              g.write(str(i))
              g.close()
              time.sleep(1)
       
except:
       #No text file? Then Create one
       f = open("text.txt","w")
       f.write(str('1')) #Giving it an input 1
       print("This file was not present so I have created one.")
       f.close()
       time.sleep(1)
       print("Re-Run the Script Now it will work the way you want.")



def read():
       with open("file.txt", 'r') as f:
              contents = f.readlines()
              print("File Says:- ")
              print(contents)
              f.close()

def write():
       with open("file.txt", 'w') as f:
              contents = f.write("Hello world")
              print("File Created")
              f.close()

try:
       read()
except:
       write()

       
       

       
       
       

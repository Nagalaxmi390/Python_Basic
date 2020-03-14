import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist") 
os.rmdir("myfolder") #will completly remove the folder from the given directory
#readlines
#open
#f.read
#f.write("")
#f.close()
#mode is to be selected
#shutil. rmtree() it comletly delets data in the folder from the os
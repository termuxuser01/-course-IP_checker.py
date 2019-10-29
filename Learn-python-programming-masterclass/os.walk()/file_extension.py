import os

root = "music"

def finder(rootdir, file_ext):  
  print(file_ext)
  print(len(file_ext))
  for dirpath, dirnames, fil in os.walk(root, topdown=True):
      for f in fil:
        if file_ext == f[-len(file_ext):]:
          print(os.path.join(dirpath, f))


finder(root, ".emp3")

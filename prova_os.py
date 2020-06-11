import os

# for root, dirs, files in os.walk(".", topdown=True):
#    for name in files:
#       if name.endswith('.pdf'):
#         #print(os.path.join(root, name))
#         print(name)
#    # for name in dirs:
#    #    print(os.path.join(root, name))

def getfiles(path):
  file_list = []
  for root, dirs, files in os.walk(path, topdown=True):
    for name in files:
      if name.endswith('.pdf'):
        file_list.append(os.path.join(root, name))
  return file_list

print(getfiles(os.getcwd()))
#python script to print a sorted table of folder sizes in the current folder
#guts of the code came from here: http://www.daniweb.com/code/snippet216951.html

import os

dirlist=os.listdir('.')
result=([])

for d in dirlist:
  if d.find('.') == -1:
    # pick a folder you have ...
    folder = d
    folder_size = 0
    for (path, dirs, files) in os.walk(folder):
      for file in files:
        filename = os.path.join(path, file)
        try:
            folder_size += os.path.getsize(filename)
        except:
            print ('strange file: ', filename)
    
    #print "Folder = %0.1f MB" % (folder_size/(1024*1024.0))
    result.append([folder_size/(1024*1024.0),folder])

#sort the results and print a table    
result.sort()
result.reverse()
for i in result:
  print ('{0:50} ==> '.format(i[1])+'%0.1f MB' %i[0])

raw_input()

import os

d = os.getcwd()

sdirs = [os.path.join(d, o) for o in os.listdir(d) 
         if os.path.isdir(os.path.join(d,o))]

ff = ['runmodel', 'runrelease', 'gfgo']
         
for d in sdirs:
    for root, directories, filenames in os.walk(d):
        #for directory in directories:
        #    print(os.path.join(root, directory)) 
        for filename in filenames: 
            fpth = os.path.splitext(filename)[0]
            if fpth in ff:
                fpth = os.path.join(root, filename)
                print('removing...{}'.format(fpth))
                os.remove(fpth)
    #break
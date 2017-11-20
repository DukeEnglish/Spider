#!/usr/bin/python  
import os  
from glob import glob  

def printSeparator(func):  
    def deco(path):  
        print("call method %s, result is:" % func.__name__)  
        # print("-" * 40)  
        func(path)  
        # print("=" * 40)  
    return deco  
@printSeparator  
def traverseDirByShell(path):  
    for f in os.popen('ls ' + path):  
        print f.strip()  
@printSeparator  
def traverseDirByGlob(path):  
    path = os.path.expanduser(path)  
    for f in glob(path + '/*'):  
        print f.strip()  
@printSeparator  
def traverseDirByListdir(path):  
    path = os.path.expanduser(path)  
    for f in os.listdir(path):  
        print f.strip()  
@printSeparator  
def traverseDirByOSWalk(path):  
    path = os.path.expanduser(path)  
    for (dirname, subdir, subfile) in os.walk(path):  
        #print('dirname is %s, subdir is %s, subfile is %s' % (dirname, subdir, subfile))  
        print('[' + dirname + ']')  
        for f in subfile:  
            print(os.path.join(dirname, f))  
if __name__ == '__main__':  
    path = r'~/laiye/mafengwo/html_new'  
#    traverseDirByGlob(path)  
#    traverseDirByGlob(path)  
    traverseDirByListdir(path)  
#    traverseDirByOSWalk(path)  

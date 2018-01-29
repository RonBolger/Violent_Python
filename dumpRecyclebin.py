#This script will search the recycle bin of a windows machine and display what is currently in it.
import os
from _winreg import *

def sid2user(sid):
    try:
        key = OpenKey(HKEY_LOCAL_MACHINE,
        "Software\Microsoft\Windows NT\CurrentVersion\ProfileList"
        + '\\' + sid)
        (value, type) = QueryValueEx(key, 'ProfileImagePath')
        user = value.split('\\')[-1]
        return user
    except:
        return sid

def returnDir():
    dirs=['C:\\Recycler\\','C:\\Recycled\\','C:\\$Recycle.Bin\\'] #recycle bin is handled differently based on windows version.
    for recycleDir in dirs:
        if os.path.isdir(recycleDir):
            return recycleDir
    return None

def findRecycled(recycleDir):
    dirList = os.listdir(recycleDir)
    for sid in dirList:
        files = os.listdir(recycleDir + sid) #will not always return readable file name, but could be a reference to the file.
        user = sid2user(sid)
        print '\n[*] Listing files for user: ' + str(user)
        for file in files:
            print '[+] Found File: ' + str(file)

def main():
    recycledDir = returnDir()
    findRecycled(recycledDir)

if __name__ == '__main__':
    main()
import os
import hashlib;
import sys;
import re
import time
reload(sys);
import warnings
warnings.filterwarnings("ignore")
def file_extension(path): 
  return os.path.splitext(path)[1]

def listFiles(dirPath):

    fileList=[]

    for root,dirs,files in os.walk(dirPath):

        for fileObj in files:

            fileList.append(os.path.join(root,fileObj))

    return fileList

def GetFileNameAndExt(filename):
    import os
    (filepath,tempfilename) = os.path.split(filename);
    (shotname,extension) = os.path.splitext(tempfilename);
    return shotname

sys.setdefaultencoding("utf-8");
def main(fileDir):

    regex = ur'FUNC_SYS_ADD_ACCDETAIL'

    fileList = listFiles(fileDir)

    for fileObj in fileList:
        if file_extension(fileObj) == '.visual':
            print(fileObj)
            f=open(fileObj,'r+')
            all_the_lines=f.readlines()
            f.seek(0)
            f.truncate()
            for line in all_the_lines:
                f.write(line.replace('SHIPMAT_PBS_Hull\t','SHIPMAT_PBS_HullX\t').replace('SHIPMAT_PBS_DeckHouse\t','SHIPMAT_PBS_DeckHouseX\t').replace('SHIPMAT_PBS_Gun\t','SHIPMAT_PBS_GunX\t').replace('SHIPMAT_PBS_Bulge\t','SHIPMAT_PBS_BulgeX\t').replace('SHIPMAT_PBS_GunDead\t','SHIPMAT_PBS_GunDeadX\t').replace('SHIPMAT_PBS_Gun_skinned\t','SHIPMAT_PBS_GunSkinnedX\t').replace('SHIPMAT_PBS_Director\t','SHIPMAT_PBS_DirectorX\t'))   
            f.close()

if os.path.exists("./gun/"):
    main("./gun/")
if os.path.exists("./ship/"):
    main("./ship/")
if os.path.exists("./director/"):
    main("./director/")
if os.path.exists("./finder/"):
    main("./finder/")
if os.path.exists("./radar/"):
    main("./radar/")
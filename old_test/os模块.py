
import os

def getALlDir(path,sp = '  '):
    filesList = os.listdir(path)
    sp += '  '
    for fileName in filesList:
        filesAbsPath = os.path.join(path, fileName)
        if os.path.isdir(filesAbsPath):
            print(sp + '目录：',fileName)
            getALlDir(filesAbsPath,sp)
        else:
            print(sp + '文件：',fileName)

getALlDir(r'E:/工作区')

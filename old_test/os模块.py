import os


def getALlDir(path, spc=''):
    filesList = os.listdir(path)
    for fileName in filesList:
        filesAbsPath = os.path.join(path, fileName)
        if os.path.isdir(filesAbsPath):
            print(spc + '目录：', fileName)
            getALlDir(filesAbsPath)
        else:
            print(spc + ' -文件：', fileName, spc + ' ')


getALlDir('E:\工作区\模板项目\DjangoBlog')

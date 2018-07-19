#!/usr/local/bin/python
# coding:utf8


import sys
reload(sys)
sys.setdefaultencoding('utf8')
import os
import random
import string


TheProjectPath = '/Users/guoxiaolei/Desktop/wealth/AZXTallyBook-master/666666'  #项目路径 直接脱进来
ThePrefix_New = 'DYC'   #类名新前缀
ThePrefix_Old = 'AZX'   #类名旧前缀
TheJunkCode_type = '' #
TheJunkCode_count = 5  #生成垃圾代码方法数量
TheJunkCode_methodslength =  16 #生成垃圾代码方法长度
TheJunkCode_outlength =  10    #生成垃圾代码方法输出长度
TheJunkCode_Dir  = ['Assets.xcassets','Base.lproj','xcodeproj','第三方','Pods','SFSMAccount.xcworkspace','SFSMAccountTests','SFSMAccountUITests','icons']  #过滤输入目录名即可

TheJunkCode_Filesuffix = ['.DS_Store','main.m','json','Info.plist']  #过滤文件名

TheJunkFilePath = ''  #垃圾文件目录
PCH_Path = '' #PCH路径
TheJunkFilePathCount = 5  #文件数量（.h.m为1个）

TheMD5FilePath = ''


alljunkfile = []  #垃圾代码文件目录

classMFiles = [] #全局.m文件拿到

classHMFiles = []  #全局.hm文件拿到

junkClassFiles = [] #全局垃圾文件记录放到PCH导入


# ----------------------------------------类名前缀修改--------------------
def modifyClassName():
    for tmpMFile in classMFiles:
        [dirmname, oldmfilename] = os.path.split(tmpMFile)
        # 获取文件名称
        #print(oldmfilename)
        # 开始修改 判断1前缀是否符合 2修改文件名前缀 3查找相同.h文件 同理4修改全局文件内容
        if (oldmfilename[0:len(ThePrefix_Old)] == ThePrefix_Old):
            filenameMNew = oldmfilename.replace(ThePrefix_Old, ThePrefix_New)
            # 2）
            os.rename(tmpMFile,dirmname+'/'+filenameMNew)
            #3）
            oldclassMindex = classHMFiles.index(tmpMFile)
            oldclassHindex =  classHMFiles.index(tmpMFile.replace('.m', '.h'))
            tmpHFile =  classHMFiles[oldclassHindex]
            [dirhname, oldHfilename] = os.path.split(tmpHFile)
            filenameHNew = oldHfilename.replace(ThePrefix_Old, ThePrefix_New)
            os.rename(tmpHFile, dirhname + '/' + filenameHNew)

            if tmpMFile.replace('.m', '.xib') in classHMFiles:
                print '进来XIB'
                oldclassXibindex = classHMFiles.index(tmpMFile.replace('.m', '.xib'))
                tmpXibFile = classHMFiles[oldclassXibindex]
                [dirxibname, oldXibfilename] = os.path.split(tmpXibFile)
                filenameXibNew = oldXibfilename.replace(ThePrefix_Old, ThePrefix_New)
                os.rename(tmpXibFile, dirxibname + '/' + filenameXibNew)
                classHMFiles[oldclassXibindex] = dirhname + '/' + filenameXibNew


            print oldclassMindex, oldclassHindex, filenameHNew
            classHMFiles[oldclassMindex] = dirmname + '/' + filenameMNew
            classHMFiles[oldclassHindex] = dirhname + '/' + filenameHNew

            for tmpHMFile in classHMFiles:
                data = ''
                file = open(tmpHMFile, "r+")
                fileContent = file.readlines()
                oldclassName =  oldmfilename[:-2] #去掉后缀.h.m
                newclassName = filenameMNew[:-2]  # 去掉后缀.h.m
                for line in fileContent:
                    if oldclassName in line:
                        print  line
                        line = line.replace(oldclassName, newclassName)
                        print  line
                        print '旧名' + oldclassName
                        print '新名' + newclassName
                    data +=line
                file.close()
                with open(tmpHMFile, 'w+') as f:
                    f.writelines(data)
# 获取所有.m文件进行
def getClassNameArr(Path):
    allfilelist = os.listdir(Path)
    for tmpFile in allfilelist:
        filepath = os.path.join(Path, tmpFile)
        if os.path.isdir(filepath):
            if 'xcodeproj' in tmpFile:
                print '过滤xcodeproj' + tmpFile
                continue
            getClassNameArr(filepath)
        elif os.path.isfile(filepath):
            if tmpFile in TheJunkCode_Filesuffix:
                print  '过滤文件' + tmpFile
                continue
            if ('.m' in tmpFile):
                classMFiles.append(filepath)
                classHMFiles.append(filepath)
            if ('.h' in tmpFile):
                classHMFiles.append(filepath)
            if ('.xib' in tmpFile):
                classHMFiles.append(filepath)

# ----------------------------------------生成垃圾代码--------------------
def addJunkCode():
    print  alljunkfile
    for tmpFile in alljunkfile:
        junkcodeStr = generate_random_str(tmpFile)
        file_data = ""
        with open(tmpFile, "r") as f:
            lines = f.readlines()  # 读取所有行
            last_line = lines[-1]  # 取最后一行
            file_data = last_line.replace('@end', junkcodeStr + '\n@end')
        print file_data
        with open(tmpFile, "w") as f:
            f.writelines([item for item in lines[:-1]])
            f.write(file_data)

def productCode(Path):
    allfilelist = os.listdir(Path)
    for tmpFile in allfilelist:
        filepath = os.path.join(Path, tmpFile)
        if os.path.isdir(filepath):
            if tmpFile in TheJunkCode_Dir:
                print '过滤目录'+tmpFile
                continue
            if 'xcodeproj' in tmpFile:
                print '过滤xcodeproj' + tmpFile
                continue
            productCode(filepath)
        elif os.path.isfile(filepath):
            if  tmpFile in TheJunkCode_Filesuffix:
                print  '过滤文件'+tmpFile
                continue
            alljunkfile.append(filepath)


#判断是路径还是文件
def isDirorFile(path):
    if os.path.isdir(path):
        return 1
    elif os.path.isfile(path):
        return 2
    else:
        return  0

def generate_random_str(filetype):
    """
    生成一个指定长度的随机字符串
    """
    random_str = '-(void)'
    base_str = 'abcdefghigklmnopqrstuvwxyz0123456789'
    base_str2 = 'abcdefghigklmnopqrstuvwxyz'
    try:
        if ('.h'  in filetype or '.m'  in filetype):
            for i in range(2):
                random_str += base_str2[random.randint(0, len(base_str2) - 1)]
            for i in range(TheJunkCode_methodslength - 6):
                random_str += base_str[random.randint(0, len(base_str) - 1)]
            random_str += '_'
            for i in range(4):
                random_str += base_str2[random.randint(0, len(base_str2) - 1)]
            # .h.m 分开混淆
            if ('.h' in filetype):
                random_str += ';'
                return random_str
            elif ('.m' in filetype):
                random_str += '{\n  NSLog(@"'
                for i in range(10):
                    random_str += base_str[random.randint(0, len(base_str)-1)]
                random_str += '");\n  [self superclass];\n}'
                return random_str

    except Exception, e:
        print ("JunkCode: %s-------%s" % (e,filetype))

# ----------------------------------------生成文件----------------------
def product_junkFile():
    base_str2 = 'abcdefghigklmnopqrstuvwxyz'
    try:
        for index in range(TheJunkFilePathCount):
            fileName = ThePrefix_New
            for i in range(8):
                fileName += base_str2[random.randint(0, len(base_str2) - 1)]
            file = open(TheJunkFilePath + fileName + '.h', 'w')
            fileContent = '#import <Foundation/Foundation.h>\n '
            fileContent += '@interface %s : NSObject \n' % (fileName)
            for ii in range(random.randint(1, 9)):
                fileContent += product_junkVar()
            fileContent += '@end'
            file.write(fileContent)

            file = open(TheJunkFilePath + fileName + '.m', 'w')
            fileContent = '#import "%s"\n ' % (fileName+'.h')
            fileContent += '@implementation %s \n' % (fileName)
            fileContent += '@end'
            file.write(fileContent)
            file.close()
            junkClassFiles.append('#import "%s"'% (fileName+'.h'))
    except Exception, e:
        print ("JunkCode: %s-------%s" % (e))

#生成随机变量
def product_junkVar():
    base_str2 = 'abcdefghigklmnopqrstuvwxyz'
    var = ''
    for i in range(10):
        var += base_str2[random.randint(0, len(base_str2) - 1)]
    var = '@property (nonatomic, copy)NSString     *%s; \n'%(var)
    return var

#把垃圾文件插入PCH中
def insertjunkFiletoPch():
    print  junkClassFiles
    importStr = ''
    for tmpFile in junkClassFiles:
        importStr+=tmpFile+'\n'
    file_data = ''
    with open(PCH_Path, "r") as f:
        for line in f:
            if '#endif' in line:
                line = line.replace('#endif', importStr + '\n#endif ')
            file_data += line
    with open(PCH_Path, "w") as f:
        f.write(file_data)

#----------------------------------------改变文件md5----------------------
def changeSingleFileMD5(file_path):
    _, file_type = os.path.splitext(file_path)
    with open(file_path, "ab") as fileObj:
        if file_type == ".png":
            text = "".join(random.sample(string.ascii_letters, 11))
        elif file_type == ".jpg":
            text = "".join(random.sample(string.ascii_letters, 20))
        elif file_type == ".lua":
            text = "\n--#*" + "".join(random.sample(string.ascii_letters, 10)) + "*#--"
        else:
            text = " "*random.randint(1, 100)
        fileObj.write(text)
        fileObj.close()
#改变文件md5
def changeFolderMD5(target_path):
    type_filter = set([".png", ".jpg", ".lua", ".json", ".plist", ".fnt"])
    for parent, folders, files in os.walk(target_path):
        for file in files:
            full_path = os.path.join(parent, file)
            _, file_type = os.path.splitext(full_path)
            if file_type in type_filter:
                changeSingleFileMD5(full_path)


#启动开始
try:
    print ('获取代码文件')
    productCode(TheProjectPath)
    print ('开始添加混淆代码')
    addJunkCode()
    print ('混淆代码添加完毕')
    # print ('获取所有M类名')
    #getClassNameArr(TheProjectPath)
    # print ('开始修改类名前缀')
    #modifyClassName()
    # print ('类名前缀修改完毕')
    print ('生成垃圾代码文件')
    #product_junkFile() #生成垃圾文件
    #insertjunkFiletoPch() #pch写入
    print ('垃圾文件添加完毕')
    print ('修改文件MD5')
    #changeFolderMD5(TheMD5FilePath)
    print ('修改完毕')
except Exception, e:
    print ("Error: %s"%(e))


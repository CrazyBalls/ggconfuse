# ggconfuse
`重要`：记得`备份X1` 记得`备份X2` 记得`备份X3`<br>
=================================
2.0版本`更新`内容：动态添加垃圾Model文件<br>
=================================

##*介绍<br>
-------
 1用来混淆IOS 目前第一版雏形上线<br>
 2以后慢慢优化增加垃圾变量 以及混淆变量 还有修改图片hash值<br>

##*功能<br>
-------
 1增加.h.m添加垃圾代码方法 自定义数量 方法长度等<br>
 2修改项目前缀<br>
 3新增垃圾代码文件<br>

##*使用方法<br>
----------
 TheProjectPath = ''  #项目路径 直接脱进来<br>
 ThePrefix_New = 'NEW'   #类名新前缀<br>
 ThePrefix_Old = 'OLD'   #类名旧前缀<br>
 TheJunkCode_type = '' #暂无↔️<br>
 TheJunkCode_count = 5  #生成垃圾代码方法数量<br>
 TheJunkCode_methodslength =  16 #生成垃圾代码方法长度<br>
 TheJunkCode_outlength =  10    #生成垃圾代码方法输出长度<br>
 TheJunkCode_Dir  = ['Assets.xcassets','Base.lproj','MJRefresh','xcodeproj','XYTableViewNoDataView']  #过滤输入目录名即可<br>
 TheJunkCode_Filesuffix = ['.DS_Store','main.m','json','Info.plist']  #过滤文件名<br>
 TheJunkFilePath = ''  #垃圾文件目录<br>
 PCH_Path = '' #PCH路径<br>
 TheJunkFilePathCount = 5  #文件数量（.h.m为1个）<br>
##*根据需求 然后运行即可 Python2 环境

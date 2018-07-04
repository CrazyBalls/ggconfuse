# ggconfuse
重要：记得备份X1 记得备份X2 记得备份X3
一介绍
 1用来混淆IOS 目前第一版雏形上线
 2以后慢慢优化增加垃圾变量 以及混淆变量 还有修改图片hash值

 二功能
 1增加.h.m添加垃圾代码方法 自定义数量 方法长度等
 2修改项目前缀
三使用方法

TheProjectPath = ''  #项目路径 直接脱进来
ThePrefix_New = 'NEW'   #类名新前缀
ThePrefix_Old = 'OLD'   #类名旧前缀
TheJunkCode_type = '' #暂无↔️
TheJunkCode_count = 5  #生成垃圾代码方法数量
TheJunkCode_methodslength =  16 #生成垃圾代码方法长度
TheJunkCode_outlength =  10    #生成垃圾代码方法输出长度
TheJunkCode_Dir  = ['Assets.xcassets','Base.lproj','MJRefresh','xcodeproj','XYTableViewNoDataView']  #过滤输入目录名即可

TheJunkCode_Filesuffix = ['.DS_Store','main.m','json','Info.plist']  #过滤文件名

根据需求 然后运行即可 

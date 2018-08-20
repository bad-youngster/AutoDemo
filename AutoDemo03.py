#coding:utf-8
import os
import shutil
import time

sourcefile = r'AutoDemo01'
destfile = 'AutoDemo03'
copycount = 0

def copyfiles(sourcefile,destfile):
    global copycount
    print(sourcefile)
    print(u"%s 当前处理文件夹%s已处理%s 个文件" %(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),sourcefile,destfile))
    for f in os.listdir(sourcefile):
        sourcef = os.path.join(sourcefile,f)
        destf = os.path.join(destfile,f)

        if os.path.isfile(sourcef):
            if not os.path.exists(destf):
                os.makedirs(destf)
            copycount += 1
            if not os.path.exists(destf) or (os.path.exists(destf) and (os.path.getsize(destf) != os.path.getsize(sourcef))):
                open(destf,"wb").write(open(sourcef,"rb").read())
                print(u"%s %s 复制完毕" %(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),destf))
            else:
                print(u"%s %s 已存在，不重复复制" %(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),destf))
        if os.path.isdir(sourcef):
            copyfiles(sourcef,destf)

if __name__ == '__main__':
    try:
        import psyco
        psyco.profile()
    except ImportError:
        pass
    copyfiles(sourcefile,destfile)




# shutil.copytree(sourcefile,destfile)


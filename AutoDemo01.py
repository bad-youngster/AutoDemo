# -*- coding:utf-8 -*-
import os

dirlist = []
filelist = []

filepath = os.getcwd()

files = os.listdir(filepath)

'''
通过列表输出文件夹和文件
忽略隐藏文件
'''

# for f in files:
#     #忽略隐藏文件
#     if (os.path.isdir(filepath + '/' + f)):
#
#         if (f[0] == '.'):
#             pass
#         else:
#             dirlist.append(f)
#
#     if (os.path.isfile(filepath + '/' + f)):
#
#         filelist.append(f)
#
# print(dirlist,filelist)

for root,dirs,files in os.walk(filepath):
    for filepath in files:
        print(os.path.join(root,filepath))

#
# allfile = []
#
# for (dirpath,dirname,filenames) in os.walk(filepath):
#     print(dirpath)
#     print(dirname)
#     print(filenames)
#     allfile.append(filenames)
#     break
#
# print(allfile)
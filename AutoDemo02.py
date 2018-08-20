# -*- coding:utf-8 -*-
import os

filepath = os.getcwd()

for root,dirs,files in os.walk(filepath):
    for filepath in files:
        print(os.path.join(root,filepath))
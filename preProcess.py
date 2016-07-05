#!/usr/bin/python 

import sys
fpIn = open("diagnosis.data","r")
attr = ['a1','a2','a3','a4','a5','a6','d1','d2']

lines = fpIn.readlines()

for line in lines:
    para = line.split("	")
    for p in para:
        print p


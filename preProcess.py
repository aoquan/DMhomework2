#!/usr/bin/python 

import sys
fpIn = open("diagnosis.data","r")
fpOut = open("preDiagnosis.data","wt")
attr = ['a1','a2','a3','a4','a5','a6','d1','d2']


lines = fpIn.readlines()
linesCount = len(lines)
for line in lines:
    para = line.split('\t')
    para0 = line.split(',')
    fpOut.write(para0[0])
    i = 0
    for p in para:
        if i > 0:
            if p == 'yes':
                fpOut.write(',')
                fpOut.write(attr[i])
        i += 1
    fpOut.write('\n')

fpIn.close()
fpOut.close()

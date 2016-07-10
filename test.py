#!/usr/bin/python 

import sys
fpIn = open("diagnosis.data","r")
attr1 = ['a2_no','a3_no','a4_no','a5_no','a6_no','d1_no','d2_no']
attr2 = ['a2_yes','a3_yes','a4_yes','a5_yes','a6_yes','d1_yes','d2_yes']


lines = fpIn.readlines()
linesCount = len(lines)
for line in lines:
    line = line.strip('\n')
    para = line.split('\t')
    para0 = line.split(',')
    i = 0

    #if para[1] == "no" and para[2] == "no" and para[3] == "yes" and para[6] == "yes" and para[7] == "no" :
    if para[1] == "no" and para[2] == "no" and para[3] == "yes" and para[6] == "yes" and "no" in para[7]:
        print line
    #a2_no,a3_no,a4_yes,d1_yes -> d2_no

fpIn.close()

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
with open('D:/slam/fej_q/resfej.txt') as file_object:
    lines=file_object.readlines() 
    file1=[]
    time=[]
    value=[] 
    for line in lines:
        row=line.split()
        if len(row)>2:
            time.append(int(row[0])-1645511782.10196+((int(row[1]))//10000)/100000)
            if len(value)>0:
                file1.append(sum(value)/len(value))
            value=[]
            value.append(float(row[2]))
        else :
            value.append(float(row[0]))
    file1.append(max(value))
    plt.plot(time[0:600],file1[0:600])
    

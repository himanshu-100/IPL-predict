# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 15:32:26 2019

@author: Himanshu Khandelwal
"""
import csv
import matplotlib.pyplot as plt
rows=[]
filename="deliveries.csv"
with open(filename, 'r',encoding="utf-8") as csvfile: 
    csvreader = csv.reader(csvfile) 
    fields = next(csvreader) 
    for row in csvreader: 
        rows.append(row)
match = []
prev='1'
temp=0
x = []
y = []
all_x = []
all_y = []
bno=0
for row in rows:
    if(row[2]=="Chennai Super Kings"):
        if(prev==row[0]):
            temp+=int(row[17])
        else:
            bno=1
            plt.plot(x,y)
            all_x.append(x)
            all_y.append(y)
            x=[]
            y=[]
            match.append(temp)
            temp=int(row[17])
            prev=row[0]
        x.append(bno)
        y.append(temp)
        bno+=1
plt.savefig('CSK.pdf')
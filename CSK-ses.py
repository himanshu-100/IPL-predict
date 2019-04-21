# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 15:32:26 2019

@author: Himanshu Khandelwal
"""
import csv
from statsmodels.tsa.holtwinters import SimpleExpSmoothing
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
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
run_on_ball = [[]]
arr=[]
for i in range(131):
    run_on_ball.append([])
for i in range(131):
    for j in range(len(all_y)):
        if(i<len(all_y[j]) and len(all_y[j])>=120):
            run_on_ball[i].append(all_y[j][i])
x_corr= []
for i in range(75):
    x_corr.append(i+1)
for i in range(131):
    rang=len(run_on_ball[i])
x1=[]
y1=[]
for i in range(120):
    data=run_on_ball[i]
    model=SimpleExpSmoothing(data)
    model_fit=model.fit()
    x1.append(i+1)
    y1.append(model_fit.predict(len(data),len(data)))
plt1.plot(x1,y1)
print(y1[len(y1)-1])
plt1.savefig('CSK-predict-SES.jpg')
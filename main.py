#!/usr/bin/env python
# coding: utf-8

# In[74]:


import numpy as np 
import pandas as pd 
from pandas import Series, DataFrame
import csv
from csv import writer
from csv import reader
import os, glob


# In[75]:


City = input("Enter the name of a city: ")
Month = input("Enter the name of a month: ")
file = City + " Factory - " + Month + " 2017.csv"
print(file)


# In[76]:


f = open("singleDataFile.csv", 'r+')
f.truncate(0)
f.close()
from glob import glob

with open('singleDataFile.csv', 'a') as singleFile:
    for csvFile in glob('*2017.csv'):
        for line in open(csvFile, 'r'):
            if "Day" not in line:
                singleFile.write(line)


# In[78]:


#This is calculating the usage as one aggregate unit


# In[79]:


days1 = 0
total_all = 0
ta = csv.reader(open('singleDataFile.csv',"r")) 
for row in ta:
    days1+=1
    total_all += int(row[1])
average = total_all // days1
print("Total amount of Kilowats is: " + str(total_all))
print("Total Average Kilowats per days is: " + str(average))



#Calculating avergae factory sq/footage
fa1 = csv.reader(open("FactoryAttributes.csv","r"))
avg_sq = 0
number_of_facts = -1
for row in fa1:
    number_of_facts +=1
    if row[2] != "SqFootage":
        amount1 = row[2]
        size1 = amount1
        number1 = int(size1.split()[0].replace(',', ''))
        avg_sq = avg_sq + number1
        
average_size1 = avg_sq // number_of_facts
average_amount_per_sq = total_all // average_size1
print("Total average per square footage: " + str(average_amount_per_sq))


# In[80]:


#This is calculating the usage per individual factory


# In[81]:


print("The metrics for " + file)
cr = csv.reader(open(file,"r")) # to skip the header 
next(cr)
total = 0
for row in cr:  
   total += int(row[1]) 
days = 0

for row in open(file):  
    days +=1

print ("Total amount of Kilowats this month: " + str(total) + " kWH ")
days = days -1
Average_Demand_Month = total // days
print ("Average Demand of Kilowats this month: " + str(Average_Demand_Month) + " kWH ")



#-----------Caluclating Sq Footage-----------------------------
fa = csv.reader(open("FactoryAttributes.csv","r"))


for row in fa: 
    if row[0] == City:
        amount = row[2]

size = amount
number = int(size.split()[0].replace(',', ''))
avg_dmnd_sqft = total//number
print("Average demand per square Foot is: " + str(avg_dmnd_sqft) + " sqr ft") 
print("The Peak Demand was at the value of: " + str(p))


# In[84]:


for csvFile1 in glob('*2017.csv'):
    file = csvFile1
    col_names = 'Day', 'Electricity Usage (kWh)'
    Month = pd.read_csv(file, header=None, names=col_names)
    Month = Month.drop(Month.index[0])
    p=Month['Electricity Usage (kWh)'].max()
    print()
    print("The metrics for " + file)
    cr = csv.reader(open(file,"r")) # to skip the header 
    next(cr)
    total = 0
    for row in cr:  
       total += int(row[1]) 
    days = 0

    for row in open(file):  
        days +=1

    print ("Total amount of Kilowats this month: " + str(total) + " kWH ")
    days = days -1
    Average_Demand_Month = total // days
    print ("Average Demand of Kilowats this month: " + str(Average_Demand_Month) + " kWH ")



    #-----------Caluclating Sq Footage-----------------------------
    fa = csv.reader(open("FactoryAttributes.csv","r"))


    for row in fa: 
        if row[0] == City:
            amount = row[2]

    size = amount
    number = int(size.split()[0].replace(',', ''))
    avg_dmnd_sqft = total//number
    print("Average demand per square Foot is: " + str(avg_dmnd_sqft) + " sqr ft") 
    print("The Peak Demand was at the value of: " + str(p))

    


# In[ ]:

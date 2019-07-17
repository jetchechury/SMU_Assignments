#!/usr/bin/env python
# coding: utf-8

# In[6]:


import os
import csv


# In[7]:


#File path
budget_data=os.path.join('/Users/jessicaetchechury/Desktop/Data_Science_Bootcamp/Homework_3/Py_Bank/budget_data.csv')


# In[9]:


#Open CSV
with open(budget_data,newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header=next(csvfile)
    print(f"Header:{csv_header}")
    #Set zero balances
    TotalMonths=0
    total=0
    Months=[]
    #Lists from csv
    Profit_Loss=[]
    for row in csvreader:
        TotalMonths += 1
        total += int(row[1])
        Months.append(row[0])
        Profit_Loss.append(int(row[1]))
    #Find the min and max values in Profit/Losses column
    maxVal=max(Profit_Loss)
    minVal=min(Profit_Loss)
    #Find the index of the min and max values so that the date can be referenced in the summary table
    maxVal_index=Profit_Loss.index(max(Profit_Loss))
    minVal_index=Profit_Loss.index(min(Profit_Loss))
    #Find average total
    average=total/TotalMonths


# In[15]:


#Print information
print("Financial Analysis""\n"
      "----------------------------""\n"
      f"Total Months:{TotalMonths}""\n"
      f"Net Total Amount:{total}""\n"
      f"Average: ${average:.2F}""\n"
      f"Maximum Value:{Months[maxVal_index]}(${(str(maxVal))})""\n"
      f"Minimum Value:{Months[minVal_index]}(${(str(minVal))})""\n"
     )


# In[16]:


#Create textfile
textfile=open('PyBudget.txt','w')
textfile.write("Financial Analysis""\n"
      "------------------------------""\n"
      f"Total Months:{TotalMonths}""\n"
      f"Net Total Amount: ${total}""\n"
      f"Average: ${average:.2F}""\n"
      f"Maximum Value:{Months[maxVal_index]}(${(str(maxVal))})""\n"
      f"Minimum Value:{Months[minVal_index]}(${(str(minVal))})""\n"
     )
textfile.close()


# In[ ]:





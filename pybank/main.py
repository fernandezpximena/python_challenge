import os
import csv
import statistics
pybank_csv = os.path.join("pybank_data.csv")

months= []
net_ammount=[]
average_change=[]
greatest_increase=0
greatest_decrease= 0

with open (pybank_csv, newline="") as csvfile:
    csvreader = csv.reader (csvfile, delimiter = ",")
    date = []
    profit_losses=[]
    for row in csvreader:
        total_month= int(row[1])
        total_loss= (sum (net_ammount))
        total_average = ((sum(average_change)/len(average_change))
print ("total months= "+ total_month)
print("net total ammount= "+ total_loss)
print("average change= "+ total_average)
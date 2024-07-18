import csv
import shutil
import random
import datetime
import sys
import time

x = 0

with open("/Users/jeffreyabbott/Downloads/sales_data.csv") as csvfile:
    myreader = csv.reader(csvfile)
    for row in myreader:
        print((row))
        
x = 1

while 0 == 0:
    shutil.copy2("/Users/jeffreyabbott/Downloads/sales_data.csv", "/Users/jeffreyabbott/Downloads/Backup/sales_data_Copy" + str(x) + ".csv")
    x = x + 1
    lastbackup = datetime.date.today()
    
    print()
    
    lines = open('/Users/jeffreyabbott/Downloads/sales_data.csv').readlines()
    lineleng = len(lines) 
    
    firstLine = lines.pop(0)
    
    print(str(lineleng) + "<")
    
    random.shuffle(lines)
    
    lines.insert(0, firstLine)
    print()
    print(lines)
    
    with open('/Users/jeffreyabbott/Downloads/sales_data.csv', 'w') as file:
        file.writelines(lines)
   
    if lastbackup > datetime.date.today(): 
        print("The last backup was " + str(lastbackup))
        print("A backup has already taken place for today, a new backup will happen tomorrow.")
        print()
        sys.exit()
    elif x > 1:
        sys.exit()
    time.sleep(10)

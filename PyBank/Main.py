import os
import csv
import shutil   # adding dependencies 

sourcepath = os.path.join("Pybank","Resources", "budget_data.csv") #path to the folder, for some reason it made me add pybank to the beginning. Not sure why 


with open(sourcepath, 'r') as csvfile:  #opening CSV file to read
    csvreader = csv.reader(csvfile, delimiter=',') #actually doing the reading 
    header = next(csvreader) #skipping the header 


    


    Count = 0 #count for the totla rows/months 
    Profit_loss = 0  #totalcount for accumulated profit and loss 
    listofprofitloss = []#list to see what the profit and loss is on a month by month basis 
    change = [] #change in the profit loss list from month to month 
    datelist = [] #list of dates that I can zip with chagne in profit and loss 
    

    for row in csvreader: # looping through the bank data 
        profitloss = int(row[1]) #what was the profit and loss for that one month 
        datelist.append(str(row[0])) #what dates are included 
        Count += 1 #counting the total month 
        Profit_loss = Profit_loss + profitloss  #summing the profit and loss by adding that months profit/loss
        listofprofitloss.append(profitloss) #lising the profit and losses by month so I can have access to all of them 
        profitmonth = [] #list of months 


   


    for x in range(1, len(listofprofitloss)): #lopping through the list of profit loss 
        nextchange = (listofprofitloss[x] - listofprofitloss[x-1]) #find the chagne in profit and loss form nmonth to mont h
        change.append(nextchange) #make a list
        
        
    

    for x in range(1,len(change)): #find total change so I can find overage chagne 
        sumofchange = change[1] + change[0]
        sumofchange2 = change[x] + change[x-1]
       


    sumchange = sum(change)
    averagechange = round(sumchange/(Count-1),2)
   

    greatestincrease = max(change) #find greetest increasde 
    greatestdecrease = min(change) #find the greatest decrease 
    zipped = zip(datelist,change) #zip the dates with the chagnes in profit and loss 
    zippedlist = iter(list(zipped))
    print(zippedlist)
    for x in zippedlist:
        if x[1] == greatestincrease: #align the right month with greatest increase 
            getdateright = next(zippedlist) #zip did not line up right, this is a correction to get the right answer
            listgetdateright = list(getdateright)
            bestdate = listgetdateright[0] #create best date variabel 
            print(bestdate)
        elif x[1] == greatestdecrease: #same as increase 
            getdateright = next(zippedlist)
            listgetdateright = list(getdateright)
            worstdate = listgetdateright[0]
            print(worstdate)

    print("Financial Analysis") #print in terminal 
    print("----------------------------")
    print(f'Total Months: {Count}')
    print(f'Total: $ {Profit_loss}')
    print(f'Average Change:: $ {averagechange}')
    print(f'Greatest Increase in Profits {bestdate} {greatestincrease}')
    print(f'Greatest Decrease in Profits {worstdate} {greatestdecrease}')
   

    

    f = open("PyBank.txt", 'w') #open a txt file 

    print("Financial Analysis", file = f)#print in text file 
    print("----------------------------", file = f)
    print(f'Total Months: {Count}', file = f)
    print(f'Total: $ {Profit_loss}', file = f)
    print(f'Average Change:: $ {averagechange}', file = f)
    print(f'Greatest Increase in Profits {bestdate} {greatestincrease}', file = f)
    print(f'Greatest Decrease in Profits {worstdate} {greatestdecrease}', file = f)

    f.close() #close txt file 

    current_loc = 'PyBank.txt' #determining where I save on my computer 
    new_loc = '/Users/clarkeallan/Desktop/python-challenge/PyBank.txt' + current_loc
    shutil.copy(current_loc, new_loc)
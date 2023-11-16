import os
import csv
import os.path
import shutil #import dependencies 

sourcepath = os.path.join("PyPoll","Resources", "election_data.csv") #establish path 



with open(sourcepath, 'r') as csvfile: #open the file 
    csvreader = csv.reader(csvfile, delimiter=',') #read the file 
    header = next(csvreader) #skip the header 

    ballots = 0 #create a ballot count 
    listofcan = [] #list of candidates 
    uniquecandidates = [] #use the list above to create a unique list 
    votecounts = [] #list of the candidates vote count 
    CharlesCount = 0 #add vote counts for charles 
    DianaCount = 0 #add counts for Diana 
    RaymonCount = 0 #add counts for Raymon 

    for row in csvreader: #go through the election data 
        ballots = ballots + 1 #add total ballots 
        candidate = str(row[2]) #list of who is runnign 
        listofcan.append(candidate)
        if candidate == "Charles Casper Stockham":
            CharlesCount = CharlesCount + 1 #count for specific individual 
        elif candidate == "Diana DeGette":
            DianaCount = DianaCount + 1 #see above 
        elif candidate == "Raymon Anthony Doane":
            RaymonCount = RaymonCount + 1 #see abvoe 
    
    CharlesPercent = round((CharlesCount/ballots)*100,3) #convert to percent and round 
    DianaPercent = round((DianaCount/ballots)*100,3)
    RaymonPercent = round((RaymonCount/ballots)*100,3)


    winner = max(CharlesCount,DianaCount,RaymonCount) #find out who has the most votes 


    for x in listofcan:
        if x not in uniquecandidates:
            uniquecandidates.append(x) #smaller list of unique candidates 


    votecounts.append(CharlesCount) #add vote counts to list 
    votecounts.append(DianaCount)
    votecounts.append(RaymonCount)
    candandvotes = zip(uniquecandidates,votecounts) #zip candidates to vote count 
    finallist = list(candandvotes) # make sure its a list 

    for x in finallist: #define winner 
        if x[1] == winner: 
            ultimatewinner = x[0]

    print("Election Results") #print in terminal 
    print("-----------------------------------------")
    print(f'Total Votes  {ballots}')
    print("----------------------------------------")
    print(f'Charles Casper Stockham: {CharlesPercent} % ({CharlesCount})')
    print(f'Diana DeGette: {DianaPercent} % ({DianaCount})')
    print(f'Raymon Anthony Doane: {RaymonPercent} % ({RaymonCount})')
    print("-----------------------------------------")
    print(f'Winner: {ultimatewinner} ')
    print("-----------------------------------------")


    f = open("PyPoll.txt", "w") #open txt file 
    print("Election Results", file =f)#populate with data 
    print("-----------------------------------------", file =f)
    print(f'Total Votes  {ballots}', file = f)
    print("----------------------------------------", file = f)
    print(f'Charles Casper Stockham: {CharlesPercent} % ({CharlesCount})', file = f)
    print(f'Diana DeGette: {DianaPercent} % ({DianaCount})', file = f)
    print(f'Raymon Anthony Doane: {RaymonPercent} % ({RaymonCount})', file =f)
    print("-----------------------------------------", file = f)
    print(f'Winner: {ultimatewinner} ', file = f)
    print("-----------------------------------------",file = f)

    f.close()#close txt file 
    current_loc = 'PyPoll.txt'
    new_loc = '/Users/clarkeallan/Desktop/python-challenge/PyPoll.txt' + current_loc#chose location to save it 
    shutil.copy(current_loc, new_loc)




    
    






    



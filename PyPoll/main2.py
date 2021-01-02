import os
import csv
csvpath = os.path.join('Resources', 'election_data.csv')
print('Election Results')
print('----------------')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    candidate=[]
    vote_count=[]
    total_votes=0
    Percent_votes =[]
    for row in csvreader:
        total_votes += 1

        if row[2] not in candidate:
            candidate.append(row[2])
            index=candidate.index(row[2])
            vote_count.append(1)
        else:
            index=candidate.index(row[2])
            vote_count[index] += 1

    for votes in vote_count:
         percentage = (votes/total_votes) * 100
         percentage = round(percentage)
         percentage = "%.3f%%" % percentage
         Percent_votes.append(percentage)

         winner = max(vote_count)
         index = vote_count.index(winner)
         winning_candidate = candidate[index]
  
    print("Total Votes:", str(total_votes))
    for i in range(len(candidate)):
        #print(candidate[i], Percent_votes[i], vote_count[i])
        print(f"{candidate[i]}: {str(Percent_votes[i])} ({str(vote_count[i])})")
    print("Winner:", (winning_candidate))
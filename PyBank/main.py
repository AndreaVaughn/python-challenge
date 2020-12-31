import os
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')
output_path = os.path.join('Analysis', 'budget_data.txt')
print("Financial Analysis") 
print("--------------------")

total_month=[]
net_total=0
Net_profit= []
change_profit=0
counter=0
Max_value=0
Min_value=0
Max_change_date=''
Min_change_date=''
writerow=[]
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        #total_month = total_month + 1 
        total_month.append(row[0])
        Net_profit.append(int(row[1]))
        net_total =+ int(row[1])
        if counter != 0:
            change_profit+=int(row[1])-previous_row
            temp_profit_row =int(row[1])-previous_row
            if (temp_profit_row) > Max_value: 
                Max_value= temp_profit_row
                Max_change_date=row[0]
            if (temp_profit_row) < Min_value:
                Min_value= temp_profit_row
                Min_change_date= row[0]
                

        previous_row= int(row[1])
        counter+=1

print('Total Months',str(len(total_month)))
print('Total:',sum(Net_profit))
print('Average Change:',round((change_profit/(counter-1)),2))
print(Max_value, Max_change_date)
print(Min_value, Min_change_date)

with open(output_path,"w") as txt_file:
    txt_file.writerow(f'Financial Analysis', '-----------------','Total Months : {str(len(total_month))}', 'Total:,sum(Net_profit))','Average Change:,round((change_profit/(counter-1)),2))', 'Max_value, Max_change_date)', 'Min_value, Min_change_date)' )

"""
This script analyzes the financial records of a company from a dataset called "budget_data.csv".
The dataset contains two columns: "Date" and "Profit/Losses". The script performs the following tasks:
 1. Calculates the total number of months in the dataset.
 2. Computes the net total amount of "Profit/Losses" over the entire period.
 3. Determines the changes in "Profit/Losses" month-over-month and calculates the average of those changes.
 4. Identifies the greatest increase in profits (the date and amount).
 5. Identifies the greatest decrease in profits (the date and amount).

 The results are then printed to the console and text file to provide a financial summary for the company.

"""
import csv
import os

#Import file from the directory and declare where the output stored  
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

total_month = 0 #counts number of months
total_net = 0 #sum of profit or loss column
averege_change = 0.00 #average of the changes month-over-month
dataset= [] #list that holds all the data from the csv file 
greatest_profit = 0 #highest profit
greatest_profit_date = str #date of highest profit
greatest_loss_date = str #greatest loss date
greatest_loss = 0 #greatest loss
value_change_sum = 0 #sum of all the changes in profit or loss month-over-month
i=0 
g=1



#open the csv and read the file
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data) 

    header = next(reader) #skip the header
   
    #loop through each rows
    for row in reader:
        total_month += 1    #count number of months
        total_net = total_net + int(row[1]) #add the profit and loss in each month
        dataset += [row]    #store each rows in to dataset list 

    """
    Now that we have stored all the rows from the CSV as a list inside a list called dataset, 
    we can calculate the difference in profit and loss from one month to another by accessing 
    the months' positions in the list. For example, if dataset = [[month1, Profit1], [month2, Profit2], ...], 
    the change in profit from month 1 to month 2 is calculated as:
        profit_change = dataset[1][1] - dataset[0][1].
    Using this concept, we can loop through each list in dataset to compute the difference in profit or loss month-over-month.
    """

    #loop through dataset       
    for x in range(len(dataset) - 1):
        value_change = int(dataset[i+1][g]) - int(dataset[i][g]) #calculate the changes in profit or loss month-over-month

        #check if the value_change is greatest profit or greatest loss 
        if value_change > greatest_profit:            
            greatest_profit = value_change
            greatest_profit_date = dataset[i+1][0]
        elif value_change < greatest_loss:
            greatest_loss = value_change
            greatest_loss_date = dataset[i+1][0]   
        #sum all value changes month-over-month    
        value_change_sum += value_change
        #next list
        i += 1
    #calculate the average of the value changes month-over-month
    averege_change = value_change_sum / (total_month -1)

    #Print results into the terminal 
    print("Financial Analysis\n\n----------------------------\n")
    print(f'Total Month: {total_month}\n\nTotal: ${total_net}\n')
    print(f'Average Change: ${round(averege_change,2)}\n')
    print(f'Greatest Increase in Profits: {greatest_profit_date} (${greatest_profit})\n')
    print(f'Greatest Decrease in Profits: {greatest_loss_date} (${greatest_loss})\n')

 #open file_to_output and write the results to txt file
with open(file_to_output, "w") as txt_file:
    txt_file.write(f"Financial Analysis\n\n----------------------------\n\n")
    txt_file.write(f"Total Month: {total_month}\n\nTotal: ${total_net}\n\n")     
    txt_file.write(f"Average Change: ${round(averege_change,2)}\n\n")
    txt_file.write(f"Greatest Increase in Profits: {greatest_profit_date} (${greatest_profit})\n\n")
    txt_file.write(f"Greatest Decrease in Profits: {greatest_loss_date} (${greatest_loss})\n")

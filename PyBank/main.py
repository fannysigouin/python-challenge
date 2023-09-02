#import os module
import os

#import csv module
import csv

#open csv file, assign to csvreader and skip header row
csvpath = os.path.join('Resources', 'budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)

    #for loop to get total months, net profit/losses, average changes of profit/losses, greatest increase and decrease
    #variable for total number of months in the period
    total_months = 0
    #variable to hold net profit/losses in the period
    net_profit_losses = 0
    #variable to hold each month's revenue in the for loop
    monthly_revenue = 0
    #variable to hold the previous month's revenue in the for loop
    previous_monthly_revenue = 0
    #list to hold changes in revenue from previous month
    revenue_change_from_previous = []
    #list to hold the month for changes in revenue
    month_change_from_previous = []
    #variable to hold average change in revenue over the period
    average_change = 0

    for row in csvreader:
        #increase total months counter by 1 for each row in the csv file as each row is a different month
        total_months += 1
        #save that month's revenue in a variable
        monthly_revenue = int(row[1])
        #increase the net profit/losses by that month's revenue
        net_profit_losses += monthly_revenue
        #if statement to exclude first month from previous revenue/change from previous revenue calculation
        
        if previous_monthly_revenue != 0:
             #calculate change in revenue compared with previous month and append to list
             #also append corresponding month to be used later for greatest increase/decrease 
            revenue_change_from_previous.append(monthly_revenue - previous_monthly_revenue)
            #append that month to the list of months with changes in revenue
            month_change_from_previous.append(row[0])
        
        #update previous month's revenue to be current month's revenue at the end of the loop
        previous_monthly_revenue = monthly_revenue
    
    #zip together revenue change and month and convert to a list
    converted_change_from_previous = list(zip(month_change_from_previous, revenue_change_from_previous))

    #get average change by summing revenue changes from previous month and dividing by total months - 1 (since there is one less change than there are months)
    average_change = round(sum(revenue_change_from_previous) / (total_months - 1), 2)

    #get greatest revenue increase 
    greatest_increase = max(revenue_change_from_previous)
    #get greatest revenue decrease
    greatest_decrease = min(revenue_change_from_previous)

    # for loop to get the corresponding month for the greatest increase and decrease in profit/losses
    greatest_increase_month = ""
    greatest_decrease_month = ""
    for month in converted_change_from_previous:
        if month[1] == greatest_increase:
            greatest_increase_month = str(month[0])
        if month[1] == greatest_decrease:
            greatest_decrease_month = str(month[0])

    print("Financial Analysis")
    print("---------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_profit_losses}")
    print(f"Average Change: ${average_change}")
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

analysis_path = 'analysis.txt'
with open(analysis_path, 'a') as file:
    file.write("Financial Analysis \n")
    file.write("--------------------------- \n")
    file.write(f"Total Months: {total_months}")
    file.write("\n")
    file.write(f"Total: ${net_profit_losses}")
    file.write("\n")
    file.write(f"Average Change: ${average_change}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")
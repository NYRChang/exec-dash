# dashboard_generator.py

import os
#import csv
import pandas
import datetime
import plotly
import plotly.graph_objects as go

while True:
    #Receive input for the Year
    year = input("Please input year of data in YYYY format (or 'end' to exit): ")
    while True:
        if year == "end":
            print("Thanks!  Please try again soon!")
            exit()
        elif len(year) != 4:
            year = input("Please re-enter year in YYYY format (ex. 2020): ")
        else:
            break

    #Receive input for the Month
    month = input("Please input month of data in MM format (or 'end' to exit): ")
    while True:
        if month == "end":
            print("Thanks!  Please try again soon!")
            exit()
        elif len(month) != 2:
            month = input("Please re-enter month in MM format (ex. July = 07): ")
        else:
            break

    #Defining the filepath
    data_period = year + month
    mydate = datetime.date(int(year), int(month), 15)
    csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "monthly-sales", str("sales-" + data_period + ".csv"))

    #Validating if file exists in the path
    try:
        os.path.exists(csv_file_path)
        df = pandas.read_csv(csv_file_path)
        break
    except FileNotFoundError:
        print("No sales data exists for that period.  Please re-enter Year and Month.")


pandas.options.display.float_format = '${:,.2f}'.format

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

#total_sales = 0
#with open(csv_file_path, "r") as csv_file: # "r" means "open the file for reading"
#    reader = csv.DictReader(csv_file) # assuming your CSV has headers
#    # reader = csv.reader(csv_file) # if your CSV doesn't have headers
#    for row in reader:
#        total_sales = total_sales + float(row["sales price"])


print("-----------------------")
print("MONTH:", mydate.strftime("%B %Y"))

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print("TOTAL MONTHLY SALES:", to_usd(df["sales price"].sum()))

print("-----------------------")
print("TOP SELLING PRODUCTS:")
top_sellers = df.groupby(["product"]).sum()
top_sellers = top_sellers.sort_values('sales price', ascending=False)
top_sellers = top_sellers.reset_index()
top_sellers.index = top_sellers.index + 1
print(top_sellers[["product" , "sales price"]].to_string(header=False))

print("-----------------------")
print("VISUALIZING THE DATA...")

chart_stats = top_sellers.to_dict("records")
#print(chart_stats)


product_category = [row["product"] for row in chart_stats]
sales_figures = [row["sales price"] for row in chart_stats]

fig = go.Figure([go.Bar(x = sales_figures, y = product_category, orientation='h', text = sales_figures, textposition='auto')])
fig.update_layout(xaxis = dict(title = 'Total Monthly Sales'), xaxis_tickangle = -45, yaxis=dict(title = 'Product', autorange="reversed"), xaxis_tickformat = '$,.2f')
fig.update_traces(texttemplate = '$%{text:,.2f}' , textposition = 'outside')
fig.update_layout(title_text = 'Top-Selling Products: ' + mydate.strftime("%B %Y"))  
fig.show()